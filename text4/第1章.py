import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='abc123456',
    database= 'text',
    port=3306
)



cursor = db.cursor()
sql = """
insert into scores(
id,name,point
)
values(null,%s,%s)
"""
name ='wangwu'
point = '34'
cursor.execute(sql,(name,point))
db.commit()

cursor.close()
