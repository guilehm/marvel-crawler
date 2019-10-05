# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CharacterItem(scrapy.Item):
    _offset = scrapy.Field()
    _limit = scrapy.Field()
    _count = scrapy.Field()
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


class SeriesItem(scrapy.Item):
    _offset = scrapy.Field()
    _limit = scrapy.Field()
    _count = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    resourceURI = scrapy.Field()
    urls = scrapy.Field()
    startYear = scrapy.Field()
    endYear = scrapy.Field()
    rating = scrapy.Field()
    type = scrapy.Field()
    modified = scrapy.Field()
    thumbnail = scrapy.Field()
    creators = scrapy.Field()
    characters = scrapy.Field()
    stories = scrapy.Field()
    comics = scrapy.Field()
    events = scrapy.Field()
    next = scrapy.Field()
    previous = scrapy.Field()

