# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 23:13:12 2021

@author: sanyuan
"""
import requests
from lxml import etree
import os
from selenium import webdriver

# def CreatePath(route):
#     file = "酷狗音乐下载\\" + route
#     if not os.path.exists(file):
#         os.mkdir(file)
#     path = os.path.abspath(file) + "\\"
#     return path
# def getHTMLText(url):
#     headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
#     "referer":"https://www.kugou.com/",
#              }
#     r = requests.get(url,headers)
#     r.raise_for_status()
#     content = r.content.decode('utf8')
#     return content
# def Doenloadsingle():
#     route = input("请输入创建的文件名字:")
#     path =  CreatePath(route)
#     flag = True
#     while flag == 1:
#         post = input("请输入你想要下载的歌曲名字，可一直输入，如若不想下载，按回车退出\n")
#         url = "https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord=" + post
        
        
#         driver_path = r"C:\chromedriver.exe"
#         option = webdriver.ChromeOptions()
#         driver = webdriver.Chrome(executable_path=driver_path,chrome_options=option)
#         driver.get(url)
#         result = driver.find_element_by_class_name("common_icon icon_play")
        
        
#         with open(real_path,'wb') as f:
#             f.write(content)
#             print(post + "下载成功!!!")
#         if post == "":
#             print("退出")
#             flag = False
#         else:
#             flag = True

post = input("歌名：")
url = "https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord=" + post
driver_path = r"C:\chromedriver.exe"
option = webdriver.ChromeOptions()    
driver = webdriver.Chrome(executable_path=driver_path,chrome_options=option)
driver.get(url)   
cover = driver.find_elements_by_xpath('//body/div[4]/div[1]/div[2]/ul[2]/li[1]/div[4]/span[1]').get_attribute('class')
print(list(cover))























