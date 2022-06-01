# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 22:29:52 2021

@author: sanyuan
"""

from queue import Queue
import requests
from lxml import etree
import os
import re
from urllib import request
import threading

#定义生产者
def producer():
    global page_queue,img_queue
    
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "referer":"https://www.doutula.com/",
                                  }
    while True:
        if page_queue.empty():
            break
        url = page_queue.get()
        response = requests.get(url,headers=headers)
        print(response.status_code)
        content = response.content.decode('utf8')
        #解析
        html = etree.HTML(content)
        #提取数据
        img_urls = html.xpath('//div[@class="page-content text-center"]//a/img/@data-original')
        alts = html.xpath('//div[@class="page-content text-center"]//a/img/@alt')
        for img_url,alt in zip(img_urls,alts):
            suffix = os.path.splitext(img_url)[1]
            alt = re.sub(r'[，。？\|\*]', '', alt)
            img_name = alt + suffix
            img_queue.put((img_url,img_name))

#定义消费者
def consumer():
    global page_queue,img_queue
    
    while True:
        if page_queue.empty() and img_queue.empty():
            break
        img = img_queue.get()
        url, filename = img
        request.urlretrieve(url, r"C:\Users\wwb\Desktop\ss\\"+ filename)
        print(filename + ' 下载成功!!')

#定义多线程
def multi_thread():
    global page_queue,img_queue
    #构造页面的安全队列
    page_queue = Queue(100)
    #构造图片的安全队列
    img_queue = Queue(500)
    
    for i in range(1,101):
        url = 'https://www.doutula.com/photo/list/?page={}'.format(i)
        page_queue.put(url)

    #定义生产者：
    for i in range(5):
        t = threading.Thread(target=producer)
        t.start()
        
    #定义消费者
    for i in range(5):
        t = threading.Thread(target=consumer)
        t.start()


multi_thread()