# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 20:49:45 2021

@author: sanyuan
"""

import requests
from lxml import etree
import os
from urllib import request
urls = []
for i in range(1,20):
    url = "https://www.doutula.com/article/list/?page={}".format(i)
    urls.append(url)
headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "referer":"https://www.doutula.com/",
        }
i = 0
for url in urls:
    try:
        r = requests.get(url,headers)
        r.encoding = r.apparent_encoding
        content = r.content.decode('utf8')
        print(r.status_code)
        html = etree.HTML(content)
        img_urls = html.xpath('//div[@class="col-xs-6 col-sm-3"]/img/@data-original')
        for img_url in img_urls:
            suffix = os.path.splitext(img_url)[1]
            path = r"C:\Users\sanyuan\Desktop\ss\\" + "img{i}".format(i) + suffix
            i = i + 1
            request.urlretrieve(img_url,path)
    except:
        continue
       
    
    











