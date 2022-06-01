# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 10:16:17 2021

@author: sanyuan
"""

import requests
from lxml import etree
import re
urls = []
for i in range(1,3):
    url = "https://list.iqiyi.com/www/1/-8------------11-{}-1-iqiyi--.html?s_source=PCW_SC".format(i)
    urls.append(url)
    
    
for url in urls:
    headers = {
        "user-agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        }
    r = requests.get(url,headers)
    r.encoding = r.apparent_encoding
    content = r.text
    a = re.findall('<div\sclass="qy-video-info-tips2 type-list".*?>\s<a\shref="(.*?)"',content,re.DOTALL)
    html = etree.HTML(content)
    detail_url = html.xpath('//div[@id="block-E"]//div/a/@href')
    print(a)
    break