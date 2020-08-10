import re
import pymysql

f = open("member.html", "r", encoding='utf')
test = re.sub('\s+', " ", f.read())

pattern = re.compile('<span>(.+?)</span> </td> <td class="td-card">.+?<span class=".+?">(.+?)</span>.+?</td> <td>(.+?)</td> <td>(.+?)</td>')
data1 = re.findall(pattern, test)
# print(data1)

db = pymysql.connect("localhost", "root", "123456", "shenzy", charset='utf8mb4')
print("成功连接数据库")

cursor = db.cursor()
sql = "insert into qqgroup(nickname, name, qq, sex) values (%s, %s, %s, %s)"
try:
    cursor.executemany(sql, data1)
    db.commit()
    print("insert success")
except Exception as e:
    print("Error", str(e), sql)

db.close()
