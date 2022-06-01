# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# from scrapy.exporters import JsonLinesItemExporter
#
# class Dytt2Pipeline(object):
#     def __init__(self):
#         self.fp = open('dytt1.json', 'wb')
#         self.expoter = JsonLinesItemExporter(self.fp, encoding='utf8')
#     def process_item(self, item, spider):
#         self.expoter.export_item(item=item)
#         return item


import pymysql

class Dytt2SpiderPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='abc123456',
            database='text',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        # print(item)
        self.cursor.execute(
            self.sql, (item['title'], item['year'],item['area'], item['category']
                       , item['lg'], item['zm'],item['show'], item['duration']
                       , item['director'], item['bjs'],item['actors'], item['profiles'])
        )
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into dytt2(id, title, year_, area, category, lg, zm, show_, duration, director,bjs,actors,profiles) values (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        return self._sql



























