# -*- coding: utf-8 -*-
import os
from urllib.parse import urlencode

import scrapy

from marvel.utils import Marvel

PRIVATE_KEY = os.getenv('PRIVATE_KEY')
PUBLIC_KEY = os.getenv('PUBLIC_KEY')

marvel = Marvel(PRIVATE_KEY, PUBLIC_KEY)


def get_full_url(url):
    return f'{url}?{urlencode(marvel.get_auth_data())}'


class CharacterSpider(scrapy.Spider):
    name = 'character'
    start_urls = ['http://gateway.marvel.com/v1/public/characters']

    def parse(self, response):
        pass
