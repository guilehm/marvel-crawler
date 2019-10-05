# -*- coding: utf-8 -*-
import os

import scrapy

from marvel.utils import Marvel

PRIVATE_KEY = os.getenv('PRIVATE_KEY')
PUBLIC_KEY = os.getenv('PUBLIC_KEY')

marvel = Marvel(PRIVATE_KEY, PUBLIC_KEY)


class CharacterSpider(scrapy.Spider):
    name = 'character'
    start_urls = ['http://gateway.marvel.com/v1/public/characters']

    def parse(self, response):
        pass
