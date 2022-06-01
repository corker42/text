# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 23:12:37 2021

@author: sanyuan
"""

import requests
from lxml import etree
import xlwt
import re

# =============================================================================
# url = "https://www.kugou.com/yy/rank/home/1-6666.html?from=rank"
# headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
#     "referer":"https://www.kugou.com/yy/rank/home/1-8888.html?from=rank",
#     }
# r = requests.get(url,headers)
# r.raise_for_status()
# 
# content = r.content.decode('utf8')
# html = etree.HTML(content)
# title = html.xpath('//div//ul//a/@title')[:29]
# real_urls = re.findall('<a\stitle=.*?href="(.*?)"',content,re.DOTALL)[1:]
# a = 0
# for real_url in real_urls:
#     headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
#     "referer":"https://www.kugou.com/",
#     }
#     r = requests.get(real_url,headers)
#     r.raise_for_status()
#     content = r.content.decode('utf8')
#     html = etree.HTML(content)
#     alls = html.xpath('//div//ul//li/@title')
#     result = []
#     for deall in alls:
#         songster = re.match(r'(.*?)-(.*?)', deall).group(1)
#         song_name = deall[len(songster)+1:]
#         dic = {
#             "歌手":songster,
#             "歌名":song_name
#             }
#         result.append(dic)
#     knob = "sheet" + str(a+1)
#     wrok = xlwt.Workbook(encoding='utf8')
#     knob = wrok.add_sheet(title[a])
#     keys = list(result[0].keys())
#     for i,key in zip(range(len(keys)),keys):
#         knob.write(0,i,key)
#     for row in range(1,len(alls)+1):
#         try:
#             for col,key in zip(range(len(keys)),keys):
#                 knob.write(row,col,result[row-1][key])
#         except:
#             continue
#     wrok.save(r"C:\Users\sanyuan\Desktop\酷狗音乐\{}.xls".format(title[a]))
#     print(title[a] + "加载完成！！！")
#     a = a + 1    
# =============================================================================
#封装为函数 ------------------------------------------------------------ 
def getHTTMLText(url):
    headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "referer":"https://www.kugou.com/",
    }
    r = requests.get(url,headers)
    r.raise_for_status()
    content = r.content.decode('utf8')
    return content
#获取所需内容
def Download1(url):
    content = getHTTMLText(url)
    html = etree.HTML(content)
    title = html.xpath('//div//ul//a/@title')[:29]
    # 获取榜单url
    real_urls = re.findall('<a\stitle=.*?href="(.*?)"',content,re.DOTALL)[1:]
    return title
def Download2(url):
    content = getHTTMLText(url)
    html = etree.HTML(content)
    # 获取榜单名和内容url
    title = html.xpath('//div//ul//a/@title')[:29]
    real_urls = re.findall('<a\stitle=.*?href="(.*?)"',content,re.DOTALL)[1:]
    return real_urls
def WriteExcel(result,title,alls,a):
    knob = "sheet" + str(a+1)
    wrok = xlwt.Workbook(encoding='utf8')
    knob = wrok.add_sheet(title[a])
    keys = list(result[0].keys())
    for i,key in zip(range(len(keys)),keys):
        knob.write(0,i,key)
    for row in range(1,len(alls)+1):
        try:
            for col,key in zip(range(len(keys)),keys):
                knob.write(row,col,result[row-1][key])
        except:
            continue
    # 创建表单并保存
    wrok.save(r"C:\Users\sanyuan\Desktop\酷狗音乐\{}.xls".format(title[a]))
    print(title[a] + "加载完成！！！")
def main():
    url = "https://www.kugou.com/yy/rank/home/1-6666.html?from=rank"
    title = Download1(url)
    real_urls = Download2(url)
    a = 0
    for real_url in real_urls:
        content = getHTTMLText(real_url)
        html = etree.HTML(content)
        alls = html.xpath('//div//ul//li/@title')
        result = []
        for deall in alls:
            # 将歌手和歌名分开
            songster = re.match(r'(.*?)-(.*?)', deall).group(1)
            song_name = deall[len(songster)+1:]
            dic = {
                "歌手":songster,
                "歌名":song_name
                }
            result.append(dic)
        WriteExcel(result,title,alls,a)
        a = a + 1
main()
        


