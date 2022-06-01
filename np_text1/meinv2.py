# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 22:11:58 2022

@author: sanyuan
"""
import re
import textwrap

import meinv1


url =  'https://www.2meinv.com/article-5310.html'
pingjie_url = url.split('.')[:-1]
pingjie_url = ''.join(pingjie_url)
pingjie_url = str(pingjie_url)
headers = {
       "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
       "Accept-Encoding":"gzip, deflate, br",
       "Referer":"https://www.2meinv.com/",
    }
content = meinv1.getHTML(url, headers).text
print(content)
name = re.findall('alt="(.*?)"',content,re.DOTALL)[0]
img_url = re.findall('<img src="(.*?)"',content,re.DOTALL)[0]
r = meinv1.getHTML(url=img_url,headers=headers)
content = r.text
# number = re.findall('<h1>\S*<span> (.*?)</span></h1>',content,re.DOTALL)
# number = number[0].split('/')[1].split(')')[0]
# number = int(number)
# cha_pic_urls = [pingjie_url + '-' + str(i) + '.html' for i in range(1,number+1)]
print(img_url)
with open('1.jpg','wb') as fp:
    fp.write(r.content)
# for cha_pic_url in cha_pic_urls:
#     img_urls =[]
#     content = meinv1.getHTML(url=cha_pic_url,headers=headers)
#     img_url = re.findall('<img src="(.*?)"',content,re.DOTALL)
#     img_urls.append(img_url)
# print(img_urls)
    #     for img_url in fenmian_urls:
    #         img_content = getHTML(url=img_url, headers=headers)
    #         # img_content = etree.HTML(img_content)
    #         # number = img_content.xpath('/html/body/div[2]/div/h1')
    #         number = re.findall('<h1>\S*<span> (.*?)</span></h1>',img_content,re.DOTALL)
    #         number = number[0].split('/')[1].split(')')[0]
    #         number = int(number)
    #         img_url = img_url.split('.')[:-1]
    #         img_url = ''.join(img_url)
    #         img_url = str(img_url)
    #         print(img_url)
    #         Fpic_urls = [img_url + '-' + str(i) + '.html' for i in range(1,number+1)]
    #         # print(pic_urls)
    #         time.sleep(1)
    # return Fpic_urls




























