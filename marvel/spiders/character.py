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

LIMIT = 13


class CharacterSpider(scrapy.Spider):
    name = 'character'
    url = 'http://gateway.marvel.com/v1/public/characters'
    start_urls = [f'{url}?{urlencode(marvel.get_auth_data())}&limit={LIMIT}']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.offset = 0
        self.limit = LIMIT
        self.count = 0

    def get_full_url(self, url):
        auth_params = urlencode(marvel.get_auth_data())
        extra_params = urlencode(dict(limit=self.limit))
        return f'{url}?{auth_params}{extra_params}'

    def parse(self, response):
        json_response = json.loads(response.body_as_unicode())
        data = json_response.get('data', {})

        if not data.get('count'):
            return

        characters = data['results']
        for character in characters:
            yield CharacterItem(**character)
