# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 22:25:02 2021

@author: sanyuan
"""

import requests
from lxml import etree
import pymysql
url = "https://s.weibo.com/top/summary?cate=realtimehot"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
           
           }
r = requests.get(url,headers)
content =r.content.decode('utf8')
html = etree.HTML(content)
pars = html.xpath('.//tr//td//a/text()')[1:-1]
hots = html.xpath('.//tr//span/text()')

for i in range(0,len(hots)):
    par = pars[i]
    hot = hots[i]
    db = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '123456.wyy',
        database = 'test',
    port = 3306 
        )
    # 创建cursor
    cursor = db.cursor()
    # 写sql语句
    sql = """
    insert into xxx(id,par,hot)
    values(null,%s,%s)
    """
    # 执行sql语句
    cursor.execute(sql,(par,hot))
    # 提交
    db.commit()
 
    # 关闭
    cursor.close()
    
    