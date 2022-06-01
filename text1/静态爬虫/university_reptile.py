# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 18:43:19 2021

@author: sanyuan
"""

#中国大学排名定向爬虫
import requests
from bs4 import BeautifulSoup
import bs4

def getHTTPText(url):
    '''1.向目标发起请求并回应'''
    try:
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        r = requests.get(url, headers, timeout = 30)
        r.raise_for_ststus()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
def fillUnvList(uList, html):
    '''2.提取信息'''
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        '''对类型做出筛选'''
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append(tds[0].string, tds[2].string, tds[3].string, tds[4].string, tds[5].string)    
    pass
def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
def main():
    uinfo = []
    url = "https://www.shanghairanking.cn/rankings/bcur/201611"
    html = getHTTPText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo,20) #20个大学
main()
