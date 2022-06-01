# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 10:24:39 2021

@author: sanyuan
"""

import requests
import time,xlwt
from selenium import webdriver
from lxml import etree
import threading
from queue import Queue

def getlinks():
    # 获取链接
    urls = []
    driver_path = r"C:\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)
    for i in range(1,2):
        url = 'https://search.jd.com/Search?keyword=%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98&suggest=1.def.0.base&wq=%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98&pvid=949af3c24d0848de80e58bc86e5ed3e5&page={}&s=1&click=0'.format(2*i-1)
        driver.get(url)
        # 控制滑动
        for j in range(6):
            js = "var q=document.documentElement.scrollTop=" + str(j*2000)
            j += 1
            driver.execute_script(js)    
            time.sleep(2)
            content = driver.page_source
            html = etree.HTML(content)
            tem_url = html.xpath("//div[@id='J_goodsList']/ul/li//div[@class='p-name p-name-type-2']/a/@href")
            urls.append(tem_url)
        print("第" + str(i) + "页爬取成功！！！")
    driver.quit()
    return urls
def getHTMLtext(tem_url):
    # 获取内容
    base_url = "https:"
    url = base_url + tem_url
    headers = {
        "origin":"https://item.jd.com",
        "referer":"https://item.jd.com/",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
              }
    r = requests.get(url,headers)
    content = r.content.decode('utf8')
    html = etree.HTML(content)
    title = html.xpath("//div[@class='sku-name']/text()").strip()
    price = html.xpath("//div[@class='dd']/span[@class='p-price']").strip()
    comment = html.xpath("//div[@id='comment-count']/a").strip()
    shop = html.xpath("//div[@class='name']/a").strip()
    data = {
           "名称":title, 
           "价格":price, 
           "评价":comment, 
           "店铺":shop, 
           }
    return data 
# tem_url = "//item.jd.com/100005926989.html"

def savedata(hard_disk):
    # 保存xlxs表
    wrok = xlwt.Workbook(encoding='utf8')
    sheet = wrok.add_sheet('京东固态硬盘')
    keys = list(hard_disk[0].keys())
    
    for i,key in zip(range(len(keys)),keys):
        sheet.write(0,i,key)
    for row in range(1,len(hard_disk)+1):
        try:
            for col,key in zip(range(len(keys)),keys):
                sheet.write(row,col,hard_disk[row-1][key])
        except:
            continue
    wrok.save(r"C:\Users\sanyuan\Desktop\京东固态硬盘.xls")

def alldatas():
    hard_disk = []
    urls = getlinks()
    for page in urls:
        for tem_url in page:
            data = getHTMLtext(tem_url)
            hard_disk.append(data)
    return hard_disk
def main():
    start = time.time()
    hard_disk = alldatas()
    savedata(hard_disk)
    end = time.time()
    print(end-start)

          
    













