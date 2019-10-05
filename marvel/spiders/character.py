# -*- coding: utf-8 -*-
import json
import os
from urllib.parse import urlencode
from marvel.items import CharacterItem
import scrapy

from marvel.utils import Marvel

PRIVATE_KEY = os.getenv('PRIVATE_KEY')
PUBLIC_KEY = os.getenv('PUBLIC_KEY')

marvel = Marvel(PRIVATE_KEY, PUBLIC_KEY)

LIMIT = 50
BASE_URL = 'http://gateway.marvel.com/v1/public'


def get_start_urls(endpoint, total, limit=LIMIT):
    return [
        f'{BASE_URL}/{endpoint}?{urlencode(marvel.get_auth_data())}&limit={limit}&offset={offset}'
        for offset in range(0, total + 1, limit)
    ]


class CharacterSpider(scrapy.Spider):
    KNOWN_QUANTITY_CHARACTERS = os.getenv('KNOWN_QUANTITY_CHARACTERS', 1500)
    name = 'character'
    start_urls = get_start_urls('characters', total=KNOWN_QUANTITY_CHARACTERS)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.offset = 0
        self.limit = LIMIT
        self.count = 0

    def get_full_url(self, url):
        auth_params = urlencode(marvel.get_auth_data())
        extra_params = urlencode(dict(limit=self.limit, offset=self.offset))
        return f'{url}?{extra_params}&{auth_params}'

    def parse(self, response):
        json_response = json.loads(response.body_as_unicode())
        data = json_response.get('data', {})
        count = data.get('count')

        if not count:
            return

        characters = data['results']
        for character in characters:
            yield CharacterItem(**character)

        self.offset += self.count
        self.count += count
