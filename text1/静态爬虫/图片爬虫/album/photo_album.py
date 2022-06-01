# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 18:40:22 2021

@author: sanyuan
"""
import requests
from lxml import etree
import time
import os

# 创建文件夹
def CreatedPath():
    flag = True
    while flag == 1:
        file = input("请输入保存数据文件夹的名称：")
        if not os.path.exists(file):
            os.mkdir(file)
            flag = False
        else:
            print('该文件已存在，请重新输入')
            flag = True
    # path = os.path.abspath(file) 获取图片的绝对路径
    path = os.path.abspath(file) + "\\"
    return path
# 下载图片
def Downloadimgs(path,img_urls,names,headers):
    name = []
    i = 0
    # 二维列表转化为一维列表
    for anony1 in names:
        for name1 in anony1:
            name.append(name1)
    for anony2 in img_urls:
        for img_url in anony2:
            r = requests.get(img_url) 
            img_path = path + name[i] +'.jpg'
            with open(img_path,'wb') as fp:
                fp.write(r.content)
                i = i + 1
                print(img_path, "   ******下载完成！")
#主程序
start = time.time()
headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
              }
path = CreatedPath()    
# 将图片名字以二维列表形式储存
urls = []
# 爬虫多少页到多少页
for i in range(2,4):
    url = "https://pic.netbian.com/4kmeinv/index_{}.html".format(i)
    urls.append(url)
    names = []
    img_urls = []
    base_url = "https://pic.netbian.com"
    for url in urls:
        r = requests.get(url,headers)
        r.encoding = r.apparent_encoding
        html = etree.HTML(r.content)
        name = html.xpath("//ul//b/text()")
        img_url = html.xpath("//ul[@class='clearfix']//li//a//img/@src")
        # 将原始地址和得到的图片地址连在一起
        img_url = list(map(lambda url:base_url + url,img_url))
        img_urls.append(img_url)
        names.append(name)
Downloadimgs(path,img_urls,names,headers)
print("全部下载完成！", "共" + str(len(os.listdir(path))) + "张图片")
end = time.time()
print("共耗时" + str(end-start) + "秒")

    
    
    














