# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 12:00:46 2021

@author: sanyuan
"""

import requests
from lxml import etree
import time
start_time = time.time()
urls = []
detail_urls = []
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
for i in range(1,5):
    url = "https://dytt8.net/html/gndy/dyzz/list_23_{}.html".format(i)
    urls.append(url)
base_url = "https://dytt8.net"
for url in urls:
    r = requests.get(url,headers = headers)
    r.encoding = r.apparent_encoding
    html = etree.HTML(r.text)
    detail_url = html.xpath('//b/a/@href')
    detail_url = list(map(lambda url:base_url + url,detail_url))#拼接
    detail_urls.append(detail_url)
movie_names = []
for page in detail_urls:
    for url in page:
        try:
            r = requests.get(url,headers = headers)
            r.encoding = r.apparent_encoding
            html = etree.HTML(r.text)
            movie_name = html.xpath('//h1/font[@color="#07519a"]/text()')
            movie_names.append(movie_name)
            
        # movie_infos = html.xpath('//div[@id="Zoom"]//text()')
        # def parse_info(movie_info,rule):
        #     return info.replace(rule,"").strip()
        # for movie_info in movie_infos:
        #         if movie_info.startswith("◎年　　代　"):
        #             Translation_name = parse_info(movie_info, "◎译　　名")
        #             print(Translation_name)
        #         elif movie_info.startswith() 
        except:
            continue
print(movie_names)
end_time = time.time()
print("总耗时{}s".format(end_time-start_time))           
        
            
    
    