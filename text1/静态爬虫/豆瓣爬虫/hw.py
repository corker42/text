#爬虫;静态网页爬取 豆瓣电影TOP50电影数据
def CreateFolder():
    """创建存储数据文件夹"""
    flag = True
    while flag == 1:
        file = input("请输入保存数据文件夹的名称：")
        if not os.path.exists(file):
            os.mkdir(file)
            flag = False
        else:
            print('该文件已存在，请重新输入')
            flag = True

    # os.path.abspath(file)  获取文件夹的绝对路径
    path = os.path.abspath(file) + "\\"
    return path

import requests
from lxml import etree
import time
import os
level = 0
start = time.time()
for I in range(0, 100, 25):   
    url = "https://movie.douban.com/top250"+"?start="+str(I)+"&filter="
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
    }
    start = time.time()
    res = requests.get(url=url, headers=headers)   # 请求
    text = res.text        # 获取请求的内容
    e = etree.HTML(text=text)    # 将请求内容转为html
    textHtml = e.xpath("//div[@class='hd']/a/@href")     # 使用xpath解析获取每一个的影片详情的链接
    for J in textHtml:
        level += 1
        print('——————————————————————————————————————————————————————————————————————————————————————————')
        res1 = requests.get(url=J, headers=headers)   # 请求每一个影片的详情
        text1 = res1.text    # 获取内容
        e1 = etree.HTML(text=text1)    # 转为html文本
        filmName = e1.xpath('//h1/span[@property="v:itemreviewed"]')   # 解析电影名称
        print(str(level)+'. 电影名称：'+filmName[0].text)
        #yearstime = e1.xpath('//h1/span[@class="year"]')
        score = e1.xpath('//div[@class="rating_self clearfix"]/strong')   # 解析评分
        print('评分为：'+score[0].text)
        textHtml1 = e1.xpath('//p[@class=" comment-content"]/span')   # 解析评论
        print('评论为：')
        for K in textHtml1:
            print(K.text)
        time.sleep(1)
    time.sleep(3)
end = time.time()
print("共耗费" + str(end - start) + "秒")