# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Practice1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 每一个爬虫的唯一标识
    name = "books"
    # 定义爬虫爬取的起始点，起始点可以是多个，我们这里是一个
    start_urls = ['http://books.toscrape.com/']
    def parse(self,response):
        # 提取数据
        # 每一本书的信息是在<article class="product_pod">中，我们使用 # css()方法找到所有这样的article 元素，并依次迭代
        for book in response.css('article.product_pod'):
            price = book.css('p.price_color::text').extract_first()
            name = book.xpath('./h3/a/@title').extract_first()
            yield {'name': name,
                   'price': price,
                   }
            next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
            if nest_url:
                next_url = response.urljoin(next_url)
                yield scrapy.Request(next_url, callback=self.parse)


