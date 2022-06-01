# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 18:53:03 2021

@author: sanyuan
"""
import requests
import re
# cc = input("你想爬取什么图片？\n")
# kw ={
#      "wold":cc
#      }
url = "https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C3%A8&fr=ala&ala=1&alatpl=normal&pos=0"
headers = {
          "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
           }
r = requests.get(url,headers)


# i = 1
# path = r"C:\Users\sanyuan\Desktop\text1\爬虫\图片爬虫\pic"

# for durl in urls:
#     try:
#         r = requests.get(durl,headers)
#         r.encoding = r.apparent_encoding
#         contents = r.content
#         if durl[-3:] == 'jpg':
#             with open('{}\pic{}.jpg'.format(path,i),'wb') as f:
#                 f.write(contents)
#         elif durl[-3:] == 'png':
#             with open('{}\pic{}.png'.format(path,i),'wb') as f:
#                 f.write(contents)
#         if durl[-3:] == 'bmp':
#             with open('{}\pic{}.bmp'.format(path,i),'wb') as f:
#                 f.write(contents)
#         if durl[-4:] == 'jpeg':
#             with open('{}\pic{}.jpeg'.format(path,i),'wb') as f:
#                 f.write(contents)
#         else:
#             continue
        
#     except:
#         continue
#     print("第{}张图片下载完成！".format(i))
#     i += 1
# print(urls)  
    
    
    
    