# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:54:58 2022

@author: sanyuan
"""

import requests
from lxml import etree
import time
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
urls =[]
for i in range(1,122):
    url = 'https://www.tuiimg.com/meinv/list_{}.html'.format(i)
    urls.append(url)
def getHTML(url,headers):
    response = requests.get(url,headers = headers)
    response.encoding = response.apparent_encoding
    content = response.text
    html = etree.HTML(content)
    return html
def meizhidizhi():
    urls =[]
    for i in range(11,15):
        url = 'https://www.tuiimg.com/meinv/list_{}.html'.format(i)
        urls.append(url)
    names_urls = []
    for url in urls:
        html = getHTML(url, headers=headers)
        names_url = html.xpath('//div/ul//li/a/@href')
        # print(names_url)
        names_urls.append(names_url)
        time.sleep(2)
    for names_url in names_urls:
        for name_url in names_url:
            urls.append(name_url)
    return urls







    
    