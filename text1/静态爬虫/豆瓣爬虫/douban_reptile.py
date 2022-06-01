# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 18:55:49 2021

@author: sanyuan
"""

# requests 获取网页信息
import requests
 
url = 'https://www.douban.com/doulist/39481377/'
headers = {
    
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
}
 
response = requests.get(url,headers=headers)
print(response)
 
html = response.text
print(html)
 
# bs4 解析获取网页信息
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"html.parser")
movie_list = soup.find("div",class_="article")
print(movie_list)
 
movies = movie_list.find_all("div",class_="doulist-item")
movie_names = []
for movie in movies:
    print(movie)
 
movie_names = []
for movie in movies:
    movie_name = movie.find("div",class_="title").get_text()
    print(movie_namnd(movie_name.strip() )  # 去除字符串前后的换行和空格
 e)
    movie_names.appe
 
for name in movie_names:
    print(name)
 
# 把数据写入本地
with open("movies.txt","w",encoding="utf-8") as f:
    for name in movie_names:
        f.write(name + '\n')