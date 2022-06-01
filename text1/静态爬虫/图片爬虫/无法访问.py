# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:48:04 2022

@author: sanyuan
"""

import requests,re
from urllib import request
from lxml import etree
url = "https://www.tuli.cc/index.html"
headers = {
       "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
       "accept-Encoding":"gzip, deflate, br",
       # "Referer":"https://www.2meinv.com/",
    }

def getHTML(url,headers):
    response = requests.get(url,headers = headers)
    response.encoding = response.apparent_encoding
    content = response.text
    # html = etree.HTML(content)
    return content
base = 'https://www.tuli.cc/'
content = getHTML(url, headers=headers)
html = etree.HTML(content)
img_urls = html.xpath('//div[@id="container"]/div/a/@href')
img_urls = [base + i for i in img_urls]
# print(img_urls)
for img_url in img_urls:
    content = getHTML(url=img_url,headers=headers)
    # print(content)
    number = re.findall('<li><a>共(.*?)页', content,re.DOTALL)[0]
    number = int(number)
    img_url = img_url.split('.')[:-1]
    img_url = ''.join(img_url)
    img_url = str(img_url)
    # print(number)
    number_urls = [img_url + '_{}.html'.format(str(i)) for i in range(1,number+1)]
    for number_url in number_urls:
        content = getHTML(url=number_url,headers=headers)
        html = etree.HTML(content)
        print(content)
        pic_urls = html.xpath('//div[@id="postarea"]/p/img/@src')
        print(pic_urls)
        break
    break
    
   
# https://www.tuli.cc/XiaoYu/11037_3.html
# https://www.tuli.cc/XiaoYu/11037_4.html