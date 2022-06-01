# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 15:40:51 2022

@author: sanyuan
"""

import requests
from lxml import etree
urls = []
for i in range(1,295):
    url = 'https://www.2meinv.com/index-{}.html'.format(i)
    urls.append(url)
headers = {
       "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
       "Accept-Encoding":"gzip, deflate, br",
       "Referer":"https://www.2meinv.com/",
    }
def getHTML(url,headers):
    response = requests.get(url,headers = headers)
    response.encoding = response.apparent_encoding
    # content = response.text
    # html = etree.HTML(content)
    return response
def fanye(urls):
    for url in urls:
        content = getHTML(url, headers=headers)
        # print(content)
        html = etree.HTML(content)
        fenmian_urls = html.xpath('/html/body/div[4]/div[1]/div[1]/div[2]/ul/li/a/@href')
        print(fenmian_urls)
        break
    return fenmian_urls


        

# Fpic_urls = fanye(urls)
# for rpic_url in Fpic_urls:
#     content = getHTML(url=rpic_url ,headers=headers)
#     img_url = re.findall('<img src="(.*?)"',content,re.DOTALL)[0]
    
    
    

# https://www.2meinv.com/article-3655.html
# https://www.2meinv.com/article-5289-3.html


