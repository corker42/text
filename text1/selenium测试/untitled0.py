# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 23:03:47 2022

@author: sanyuan
"""

import pandas as pd
#解决数据输出时列名不对齐的问题
# pd.set_option('display.unicode.east_asian_width', True)
# df = pd.DataFrame({
#     '语文':[110,105,99],
#      '数学':[105,88,115],
#      '英语':[109,120,130],
#       '班级':'高一7班'
# },index=[0,1,2])
# print(df)
# # 创建数据
# data = {'A': ['A1','A1','A3'],
#          'B': ['B1','B2','B1']}
# data__frame = pd.DataFrame(data)  # 创建DataFrame对象
# data__frame.drop_duplicates('A',inplace=True)  # 指定列名为A
# print(data__frame)                              # 打印移除后的数据

# # 创建数据
# data = {'A': ['A1','A1','A1','A2','A2'],
#         'B': ['B1','B1','B3','B4','B5'],
#         'C': ['C1', 'C2', 'C3','C4','C5']}
# data__frame = pd.DataFrame(data)  # 创建DataFrame对象
# data__frame.drop_duplicates(subset=['A','B'],inplace=True)  # 进行多列去重操作
# print(data__frame)                                           # 打印移除后的数据

# pd.set_option('display.unicode.east_asian_width', True)
# data = [['Aaron',18,'boy'],['Abby',23,'girl']]    # 创建数据
# columns = ['name','age','sex']      # 创建列名
# df = pd.DataFrame(data=data, columns=columns) # 创建DataFrame对象
# print('原数据如下：\n',df)
# tuples = tuple(tuple(t) for t in df.values)  # 将DataFrame数据转换为元组数据
# print('转换后的元组数据如下：\n',tuples)

#设置数据显示的列数和宽度
# pd.set_option('display.max_columns',500)
# pd.set_option('display.width',1000)
# #解决数据输出时列名不对齐的问题
# pd.set_option('display.unicode.east_asian_width', True)
# df1=pd.read_csv(r'C:\Users\sanyuan\Desktop\1. 示例源码--Python网络爬虫从入门到精通\示例源码--Python网络爬虫从入门到精通\12\21\1月.txt',sep='\t',encoding='gbk')
# print(df1.head())
# print(df1['收货人姓名'])

# df = pd.DataFrame()
# url_list = ['http://www.espn.com/nba/salaries/_/seasontype/4']
# for i in range(2, 13):
#     url = 'http://www.espn.com/nba/salaries/_/page/%s/seasontype/4' % i
#     url_list.append(url)
# #遍历网页中的table读取网页表格数据
# for url in url_list:
#     df = df.append(pd.read_html(url), ignore_index=True)
# #列表解析：遍历dataframe第3列，以子字符串$开头
# df = df[[x.startswith('$') for x in df[3]]]
# print(df)
# df.to_csv(r'C:\Users\sanyuan\Desktop\1. 示例源码--Python网络爬虫从入门到精通\示例源码--Python网络爬虫从入门到精通\12\22\NBA.csv',header=['RK','NAME','TEAM','SALARY'], index=False)

# excelFile = r'C:\Users\sanyuan\Desktop\1. 示例源码--Python网络爬虫从入门到精通\示例源码--Python网络爬虫从入门到精通\12\26\books.xls'
# dfrow = pd.DataFrame(pd.read_excel(excelFile))
# #设置数据显示的列数和宽度
# pd.set_option('display.max_columns',500)
# pd.set_option('display.width',1000)
# #解决数据输出时列名不对齐的问题
# pd.set_option('display.unicode.ambiguous_as_wide', True)
# pd.set_option('display.unicode.east_asian_width', True)


# print('-------------------------按行数据排序-------------------------')
# #按照索引值为0的行，即第一行的值升序排序
# print(dfrow.sort_values(by=0,ascending=True,axis=1))

#解决数据输出时列名不对齐的问题
# pd.set_option('display.unicode.east_asian_width', True)
# data = [[110,105,99],[105,88,115],[109,120,130]]
# index = [1,2,3]
# columns = ['语文','数学','英语']
# df = pd.DataFrame(data=data, index=index, columns=columns)
# df['总成绩']=df.sum(axis=0)
# print(df)

#解决数据输出时列名不对齐的问题
# pd.set_option('display.unicode.east_asian_width', True)
# data = [[110,105,99],[105,88,115],[109,120,130],[112,115]]
# index = [1,2,3,4]
# columns = ['语文','数学','英语']
# df = pd.DataFrame(data=data, index=index, columns=columns)
# new=df.mean()
# #增加一行数据（语文、数学和英语的平均值,忽略索引）
# df=df.append(new,ignore_index=True)
# print(df)

#设置数据显示的列数和宽度
# pd.set_option('display.max_columns',500)
# pd.set_option('display.width',1000)
# #解决数据输出时列名不对齐的问题
# pd.set_option('display.unicode.east_asian_width', True)
# df=pd.read_csv(r'C:\Users\sanyuan\Desktop\1. 示例源码--Python网络爬虫从入门到精通\示例源码--Python网络爬虫从入门到精通\12\33\JD.csv',encoding='gbk')
# #抽取数据
# df1=df[['一级分类','7天点击量','订单预定']]
# print(df1.groupby('一级分类').sum())#分组统计求和
# # 抽取数据
# df1=df[['一级分类','二级分类','7天点击量','订单预定']]
# print(df1.groupby(['一级分类','二级分类']).sum())#分组统计求和

# # 抽取数据
# df1=df[['一级分类','二级分类','7天点击量','订单预定']]
# print(df1.groupby('二级分类')['7天点击量'].sum())

from sklearn.learning_curve import learning_curve
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

















