# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class Dm5Pipeline(object):
#     def process_item(self, item, spider):
#         return item

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from dm5.settings import IMAGES_STORE as IMGS

class Dm5DownloadPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_urls = item['image_urls']
        for image_url in image_urls:
            yield Request(image_url, meta={'item':item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        name = item['name']
        pic_path = IMGS + name + '.jpg'
        return pic_path
