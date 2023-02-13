# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qsbk.items import QsbkItem

class QsbkSpider(CrawlSpider):
    name = 'qsbk_'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    rules = (
        Rule(LinkExtractor(allow=r'.+page/\d+/'),  follow=True),
        Rule(LinkExtractor(allow=r'.+article/\d{9}'), callback='parse_item',follow=False),
    )

    def parse_item(self, response):
        author = response.xpath('//span[@class="side-user-name"]/text()').get()
        rate = response.xpath('//div[@class="side-detail"]/div[@class="side-line1"]/text()').getall()[0]
        fans = response.xpath('//div[@class="side-detail"]/div[@class="side-line1"]/text()').getall()[1]
        qs = response.xpath('//div[@class="side-detail"]/div[@class="side-line1"]/text()').getall()[2]
        content = response.xpath('//div[@class="content"]//text()').getall()
        content = "".join(content).strip()
        item = QsbkItem(author=author,rate=rate,fans=fans,qs=qs, content=content)
        yield item
        # print(author, rate,fans,qs)
        # print(content)