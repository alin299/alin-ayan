#!/usr/bin/python3
"""
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "shenzy")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()
"""

import pymysql #数据库

db = pymysql.connect("localhost", "root", "123456", "shenzy")
print("成功连接数据库")

cursor = db.cursor()
sql = "insert into qqgroup values('沈泽燕', '客', 1131155495, '女')"
print(sql)

try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

db.close()
