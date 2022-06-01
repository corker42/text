# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 09:47:33 2022

@author: sanyuan
"""
"""
爬虫目标：爬取 https://www.bbiquge.net/fenlei/1_1/ 有封面的六部小说
需要爬取的内容：1.封面图片 2.小说名字 3.小说简介 4.小说具体内容
将爬取的内容保存在指定目录下，采用多线程爬取
"""

import requests
import os,time
from lxml import etree
# from queue import Queue
# import threading

def get_base_content(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Referer":"https://www.bbiquge.net/",
        "Cookie":"Hm_lvt_cc13cd690e17410a96647c14d9e29aba=1644113098; Hm_lvt_a6e0e6155afbc85db439c009f957f6d4=1644113098; jieqiVisitTime=jieqiArticlesearchTime%3D1644114148; jieqiVisitId=article_articleviews%3D12613%7C24879; PHPSESSID=rppphnuqdigg83k8fg56re8428; jieqiUserInfo=jieqiUserId%3D52037%2CjieqiUserName%3D%D4%AA%2CjieqiUserGroup%3D3%2CjieqiUserName_un%3D%26%23x5143%3B%2CjieqiUserLogin%3D1644116556; jieqiVisitInfo=jieqiUserLogin%3D1644116556%2CjieqiUserId%3D52037; Hm_lpvt_cc13cd690e17410a96647c14d9e29aba=1644116563; Hm_lpvt_a6e0e6155afbc85db439c009f957f6d4=1644116563",
        "Accept-Encoding":"gzip, deflate, br",
        }
    response = requests.get(url=url,headers=headers)
    response.encoding = response.apparent_encoding
    content = response.text
    # print(response.status_code,content[:1000])
    return content
    
def get_base_info(content):
    # 获取书名和url
    html = etree.HTML(content)
    novel_names = html.xpath('//div[@class="item"]/div/a/@title')
    novel_urls = html.xpath('//div[@class="item"]//div[@class="pic"]/a/@href')
    # print(novel_names,novel_urls)
    all_names = list(zip(novel_names,novel_urls))
    return all_names

def greategile(all_names,path):
    # 创建相关文件夹 并下载图片和简介
    for novel_name,novel_url in all_names:
        os.makedirs(path + "\\" + novel_name)
    for novel_name,novel_url in all_names:
        content = get_base_content(url=novel_url)
        html = etree.HTML(content)
        novel_pic = html.xpath('//div[@id="picbox"]/div/img/@src')
        # novel_pic = novel_pic[0]
        # print(novel_pic)
        novel_intr = html.xpath('//div[@id="info"]//div[@id="intro"]/text()')
        novel_intr = ''.join(novel_intr).strip()
        # print(novel_pic,novel_intr)
        # request.urlretrieve(novel_pic,path + "./" + novel_name + "./封面.jpg")
        # path = path + "\\" + novel_name
        # os.makedirs(path)
        # 注意url不能有引号
        r = requests.get(url=novel_pic[0])
        with open(path + "\\" + novel_name +  "\\" + "封面.jpg",'wb') as fp:
            fp.write(r.content)
        with open(path + "\\" + novel_name +  "\\" + "小说简介.txt",'w',encoding='utf8') as fp:
            fp.write(novel_intr)
            
# def producer():
#     global u_queue,c_queue
#     while True:
#         if u_queue.empty():
#             break
#         url = u_queue.get()
#         content = get_base_content(url=url)
#         html = etree.HTML(content)
#         title = html.xpath('//*[@id="main"]/h1')
#         details = html.xpath('//*[@id="content"]/text()')
#         details = ''.join(details)
#         details = details.replace('\r\r', '\n').replace('\xa0', ' ')
#         c_queue.put(title,details)
        
# def consumer():
#     global u_queue,c_queue
#     while True:
#         if u_queue.empty() and c_queue.empty():
#             break
#         neirong = c_queue.get()
#         title,details = neirong
#         with open('name' + '.txt', 'a+', encoding='utf-8') as file:
#             file.write(title + '\n')
#             file.write(details)

# def muli_thread(all_names):
#     global u_queue,c_queue
#     u_queue = Queue(500)
#     c_queue = Queue(600)
#     for novel_name,novel_url in all_names:
#         content = get_base_content(url=novel_url)
#         html = etree.HTML(content)
#         urls = html.xpath('/html/body/div[4]/dl/dd/a/@href')
#         urls = [novel_url + url for url in urls]
#         for url in urls:
#             u_queue.put(url)
#             break
#     #定义生产者
#     for i in range(5):
#          t = threading.Thread(target=producer)
#          t.start() 
#      #定义消费者
#     for i in range(5):
#          t = threading.Thread(target=consumer)
#          t.start()
    
        
if __name__ == '__main__':
    # 主程序
    start_time = time.time()
    url = "https://www.bbiquge.net/"
    path = r"C:\Users\sanyuan\Desktop\笔趣阁小说"
    content = get_base_content(url)
    all_names = get_base_info(content)
    greategile(all_names, path)
    # muli_thread(all_names)
    end_time = time.time()
    print(end_time-start_time)
        









    
    
    
    
    
    
    
    
    
    
    
    