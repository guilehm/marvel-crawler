# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CharacterItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    modified = scrapy.Field()
    thumbnail = scrapy.Field()
    resourceURI = scrapy.Field()
    comics = scrapy.Field()
    series = scrapy.Field()
    stories = scrapy.Field()
    events = scrapy.Field()
    urls = scrapy.Field()
