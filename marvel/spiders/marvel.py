# -*- coding: utf-8 -*-
import json
import os
from urllib.parse import urlencode
from marvel.items import CharacterItem, SeriesItem, ComicItem
import scrapy

from marvel.utils import Marvel

PRIVATE_KEY = os.getenv('PRIVATE_KEY')
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
LIMIT = 100
BASE_URL = 'http://gateway.marvel.com/v1/public'
MARVEL = Marvel(PRIVATE_KEY, PUBLIC_KEY)


def get_start_urls(endpoint, stop, start=0, limit=LIMIT):
    return [
        f'{BASE_URL}/{endpoint}?{urlencode(MARVEL.get_auth_data())}&limit={limit}&offset={offset}'
        for offset in range(int(start), int(stop) + 1, limit)
    ]


class BaseSpider(scrapy.Spider):
    name = None
    item = None
    known_quantity = None
    start_urls = []
    start = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.item = self.item
        self.offset = 0
        self.limit = LIMIT
        self.count = 0

    def get_full_url(self, url):
        auth_params = urlencode(MARVEL.get_auth_data())
        extra_params = urlencode(dict(limit=self.limit, offset=self.offset))
        return f'{url}?{extra_params}&{auth_params}'

    def parse(self, response):
        json_response = json.loads(response.body_as_unicode())
        data = json_response.get('data', {})
        count = data.get('count')

        if not count:
            return

        items = data['results']
        for item in items:
            self.count += 1
            yield self.item(
                _offset=self.offset,
                _limit=self.limit,
                _count=self.count,
                **item
            )
        self.offset += self.count


class CharacterSpider(BaseSpider):
    name = 'characters'
    item = CharacterItem
    known_quantity = os.getenv('KNOWN_QUANTITY_CHARACTERS')
    start_urls = get_start_urls('characters', start=0, stop=known_quantity)


class SeriesSpider(BaseSpider):
    name = 'series'
    item = SeriesItem
    known_quantity = os.getenv('KNOWN_QUANTITY_SERIES')
    start_urls = get_start_urls('series', start=0, stop=known_quantity)


class ComicSpider(BaseSpider):
    name = 'comics'
    item = ComicItem
    known_quantity = os.getenv('KNOWN_QUANTITY_COMICS')
    start_urls = get_start_urls('comics', start=0, stop=known_quantity)
