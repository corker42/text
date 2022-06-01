# -*- coding: utf-8 -*-
import scrapy
from dm5.items import Dm5Item

class Dm5Spider(scrapy.Spider):
    name = 'dm5_'
    allowed_domains = ['dm5.com']
    start_urls = []
    for i in range(1,4,1):
        url = 'https://www.dm5.com/manhua-list-p{}/'.format(i)
        start_urls.append(url)

    def parse(self, response):
        # print(response.text)
        detai_urls = response.xpath('//div[@class="mh-item-tip"]/a/@href').getall()
        for detai_url in detai_urls:
            detai_url = 'https://www.dm5.com' + detai_url
            yield scrapy.Request(detai_url, self.parse_detail_url)
    def parse_detail_url(self, response):
        name = response.xpath('//div[@class="info"]/p[@class="title"]/text()').get().strip()
        pic_url = response.xpath('//div[@class="cover"]/img/@src').get()
        item = Dm5Item(image_urls=[pic_url], name=name)
        yield item
