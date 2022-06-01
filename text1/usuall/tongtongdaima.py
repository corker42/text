# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 19:08:25 2021

@author: sanyuan
"""
import requests
from lxml import etree

url = "https://s.weibo.com/top/summary?cate=realtimehot"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
           
           }
r = requests.get(url,headers)
content =r.content.decode('utf8')
html = etree.HTML(content)
pars = html.xpath('.//tr//td//a/text()')[1:]
hots = html.xpath('.//tr//span/text()')
xxl = []
for i in range(0,len(hots)):
    hh = {
        "内容":pars[i],
        "热度":hots[i]
        }
    xxl.append(hh)
print(xxl)


# 创建Excel表并保存
# import xlwt
# wrok = xlwt.Workbook(encoding='utf8')
# sheet = wrok.add_sheet('新浪热搜')

# keys = list(xxl[0].keys())

# for i,key in zip(range(len(keys)),keys):
#     sheet.write(0,i,key)
# for row in range(1,len(pars)+1):
#     try:
#         for col,key in zip(range(len(keys)),keys):
#             sheet.write(row,col,xxl[row-1][key])
#     except:
#         continue
# wrok.save(r"C:\Users\sanyuan\Desktop\新浪热搜.xls")


# 创建csv文件导出
import csv
headers = list(xxl[0].keys())

with open(r"C:\Users\sanyuan\Desktop\新.csv",'w',newline='') as f:
          writer = csv.DictWriter(f, headers,delimiter='|')
          writer.writeheader()
          writer.writerows(xxl)







