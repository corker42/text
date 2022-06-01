# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 17:34:52 2021

@author: sanyuan
"""

import requests
import time,os
from lxml import etree
import threading,re
from queue import Queue
from urllib import request
path = r'C:\Users\sanyuan\Desktop\bian'
def GreateFile(path):
    #创建主文件
    
    os.makedirs(path)
    #获取下一级文件名及目标链接
    url = "https://pic.netbian.com/"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Referer":"https://pic.netbian.com/",
             }
    r = requests.get(url,headers=headers)
    r.encoding = r.apparent_encoding
    html = etree.HTML(r.text)
    Subdir_name = html.xpath('//div[@class="classify clearfix"]/a/@title')
    Sub_url = html.xpath('//div[@class="classify clearfix"]/a/@href')
    #拼接目标url
    Target_url = [url + str(i) for i in Sub_url]
    #创建次级目录
    for name in Subdir_name:
        os.makedirs(path + "./" + name)
    return (Target_url,Subdir_name)

def Producer():
    #定义生产者
    global page_queue, img_queue,Target
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Referer":"https://pic.netbian.com/",
             }
    while True:
        #如果队列为空，则停止抓取
        if page_queue.empty():
            break
        page_url = page_queue.get()
        r = requests.get(url=page_url,headers=headers)
        r.encoding = r.apparent_encoding
        html = etree.HTML(r.text)
        #提取图片地址和图片名字
        img_urls = html.xpath("//ul[@class='clearfix']//li//a//img/@src")
        #拼接图片地址
        url = "https://pic.netbian.com"
        pic_urls = [url + str(i) for i in img_urls]
        pic_names = html.xpath("//ul//b/text()")
        for pic_url,pic_name in zip(pic_urls,pic_names):
            #切割图片格式
            suffix = os.path.splitext(pic_url)[1]
            pic_name = re.sub(r'[，。？\|\*]', '', pic_name)
            pic_name = pic_name + suffix
            img_queue.put((pic_url,pic_name))
            
def Consumer(count):
    #定义消费者
    global page_queue,img_queue,Target
    while True:
        if page_queue.empty() and img_queue.empty():
            break
        img = img_queue.get()
        url,filename = img
        img_path = path + "./" + Target[1][count]
        request.urlretrieve(url,img_path + "./" + filename)
        print(filename + '下载成功！！！')

def Multi_thread(count,page=3):
    #定义多线程
    global page_queue,img_queue,Target
    #构造页面安全队列
    page_queue = Queue(100)
    #构造图片的安全队列
    img_queue = Queue(500)
    for i in range(1,page):
        url = "{}/index_{}.html".format(Target[0][count], i)
        page_queue.put(url)
    
    #定义生产者(5线程)
    for i in range(5):
        t = threading.Thread(target=Producer)
        t.start()
        time.sleep(3)
    #定义消费者(5线程)
    for i in range(5):
        t = threading.Thread(target=Consumer)
        t.start()
        time.sleep(3)
if __name__ == "__main__":
    #主程序
    path = r'C:\Users\sanyuan\Desktop\bian'
    Target = GreateFile(path)
    #page = input("要爬取的的页数?\n")
    #page = int(page) + 1
    start = time.time()
    for count in range(12):
        print("***************正在爬取第"+str(count+1)+"项************")
        Multi_thread(count)
        print("**************第"+str(count+1)+"项爬取完毕**************")
    end = time.time()
    print("共耗时" + str(end-start) + "秒")    
    







    


















