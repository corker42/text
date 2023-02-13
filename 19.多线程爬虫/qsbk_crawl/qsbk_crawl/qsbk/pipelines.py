# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter

class QsbkPipeline(object):
    def __init__(self):
        self.fp = open('qsbk.json', 'wb')
        self.expoter = JsonLinesItemExporter(self.fp, encoding='utf8')
    def process_item(self, item, spider):
        self.expoter.export_item(item)
        return item
