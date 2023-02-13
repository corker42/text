# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 10:35:51 2021

@author: sanyuan
"""

import requests, threading
from lxml import etree
from queue import Queue
import tkinter


class Novel(threading.Thread):
    def __init__(self, novelurl_list=None, name_list=None):
        super().__init__()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Referer': 'http://www.xbiquge.la/7/7931/',
            'Cookie': '_abcde_qweasd=0; BAIDU_SSP_lcr=https://www.baidu.com/link?url=jUBgtRGIR19uAr-RE9YV9eHokjmGaII9Ivfp8FJIwV7&wd=&eqid=9ecb04b9000cdd69000000035dc3f80e; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1573124137; _abcde_qweasd=0; bdshare_firstime=1573124137783; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1573125463',
            'Accept-Encoding': 'gzip, deflate'
        }
        self.novelurl_list = novelurl_list
        self.name_list = name_list

    # 获取网站源码
    def get_text(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = 'utf-8'
        return response.text

    # 获取小说的信息
    def get_novelinfo(self):
        while True:
            if self.name_list.empty() and self.novelurl_list.empty():
                break
            url = self.novelurl_list.get()
            # print(url)
            html = etree.HTML(self.get_text(url))
            name = self.name_list.get()  # 书名
            # print(name)
            title_url = html.xpath('//div[@id="list"]/dl/dd/a/@href')
            title_url = ['http://www.xbiquge.la' + i for i in title_url]  # 章节地址
            titlename_list = html.xpath('//div[@id="list"]/dl/dd/a/text()')  # 章节名字列表
            self.get_content(title_url, titlename_list, name)

    # # 获取小说每章节的内容
    def get_content(self, url_list, title_list, name):
        for i, url in enumerate(url_list):
            item = {}
            html = etree.HTML(self.get_text(url))
            content_list = html.xpath('//div[@id="content"]/text()')
            content = ''.join(content_list)
            content = content + '\n'
            item['title'] = title_list[i]
            item['content'] = content.replace('\r\r', '\n').replace('\xa0', ' ')
            # print(item)
            with open(name + '.txt', 'a+', encoding='utf-8') as file:
                file.write(item['title'] + '\n')
                file.write(item['content'])

   #------------------通过多线程，返回每本书的名字和每本书的连接
    def get_name_url(self):
        base_url = 'http://www.xbiquge.la/xiaoshuodaquan/'
        html = etree.HTML(self.get_text(base_url))
        novelurl_list = html.xpath('//div[@class="novellist"]/ul/li/a/@href')
        name_list = html.xpath('//div[@class="novellist"]/ul/li/a/text()')
        return novelurl_list, name_list

    def run(self):
        self.get_novelinfo()


if __name__ == '__main__':
    n = Novel()
    url_list, name_list = n.get_name_url()
    name_queue = Queue()
    url_queue = Queue()
    for url in url_list:
        url_queue.put(url)
    for name in name_list:
        name_queue.put(name)

    crawl_list = [1, 2, 3, 4, 5]  # 定义五个线程
    for crawl in crawl_list:
        # 实例化对象
        novel = Novel(name_list=name_queue, novelurl_list=url_queue)
        novel.start()

