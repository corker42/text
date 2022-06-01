# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 21:48:07 2021

@author: sanyuan
"""

import pymysql
# 打开数据连接
db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '123456.wyy',
    database = 'test',
    port = 3306
    )
# 使用cursor()创建一个游标对象
cursor = db.cursor()
# # 书写sql语句
# sql =  """
# insert into scores(id,name,points)
# values(2,'李四',66)
# """
# # 执行语句
# cursor.execute(sql)
# # 提交SQL语句
# db.commit()
sql =  """
insert into scores(id,name,points)
values(null,%s,%s)
"""
name = '王五'
points = 90
# 执行语句
cursor.execute(sql,(name,points))

# 提交SQL语句
db.commit()





#关闭连接
cursor.close
