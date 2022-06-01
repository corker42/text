# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Dytt2Item(scrapy.Item):
    title = scrapy.Field()
    year = scrapy.Field()
    area = scrapy.Field()
    category = scrapy.Field()
    lg = scrapy.Field()
    zm = scrapy.Field()
    show = scrapy.Field()
    duration = scrapy.Field()
    director = scrapy.Field()
    bjs = scrapy.Field()
    actors = scrapy.Field()
    profiles = scrapy.Field()