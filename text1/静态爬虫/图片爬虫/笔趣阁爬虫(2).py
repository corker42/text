# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 09:47:33 2022

@author: sanyuan
"""
"""
爬虫目标：爬取 https://www.bbiquge.net/fenlei/1_1/ 有封面的六部小说
需要爬取的内容：1.封面图片 2.小说名字 3.小说简介 4.小说具体内容
将爬取的内容保存在指定目录下，采用多线程爬取
"""

import requests
import time
from lxml import etree


start_time = time.time()
url = "https://www.bbiquge.net/"
path = r"C:\Users\sanyuan\Desktop\笔趣阁小说"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Referer":"https://www.bbiquge.net/",
    "Cookie":"Hm_lvt_cc13cd690e17410a96647c14d9e29aba=1644113098; Hm_lvt_a6e0e6155afbc85db439c009f957f6d4=1644113098; jieqiVisitTime=jieqiArticlesearchTime%3D1644114148; jieqiVisitId=article_articleviews%3D12613%7C24879; PHPSESSID=rppphnuqdigg83k8fg56re8428; jieqiUserInfo=jieqiUserId%3D52037%2CjieqiUserName%3D%D4%AA%2CjieqiUserGroup%3D3%2CjieqiUserName_un%3D%26%23x5143%3B%2CjieqiUserLogin%3D1644116556; jieqiVisitInfo=jieqiUserLogin%3D1644116556%2CjieqiUserId%3D52037; Hm_lpvt_cc13cd690e17410a96647c14d9e29aba=1644116563; Hm_lpvt_a6e0e6155afbc85db439c009f957f6d4=1644116563",
    "Accept-Encoding":"gzip, deflate, br",
    }
response = requests.get(url=url,headers=headers)
response.encoding = response.apparent_encoding
content = response.text
html = etree.HTML(content)
novel_names = html.xpath('//div[@class="item"]/div/a/@title')
novel_urls = html.xpath('//div[@class="item"]//div[@class="pic"]/a/@href')
# print(novel_names)
for i,novel_url in enumerate(novel_urls):
    response = requests.get(url=novel_url,headers=headers)
    response.encoding = response.apparent_encoding
    content = response.text
    html = etree.HTML(content)
    chapter_urls = html.xpath('/html/body/div[4]/dl/dd/a/@href')
    chapter_urls = [novel_url + a for a in chapter_urls]
    chapter_names = html.xpath('/html/body/div[4]/dl/dd/a/text()')
    for j,chapter_url in enumerate(chapter_urls):
        item = {}
        response = requests.get(url=chapter_url,headers=headers)
        response.encoding = response.apparent_encoding
        content = response.text
        html = etree.HTML(content)
        content = html.xpath('//*[@id="content"]/text()')
        content = ''.join(content)
        content = content + '\n'
        item['title'] = chapter_names[j]
        item['content'] = content.replace('\r\r', '\n').replace('\xa0', ' ')
        print(item)
        with open(novel_names[i] + '.txt', 'a+', encoding='utf-8') as file:
            file.write(item['title'] + '\n')
            file.write(item['content'])
    

        
        









    
    
    
    
    
    
    
    
    
    
    
    