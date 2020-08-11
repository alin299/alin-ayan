#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class QQgroup(Base):
    # 表的名字:
    __tablename__ = 'qqgroup'

    # 表的结构:
    name = Column(String(20))
    nickname = Column(String(20))
    qq = Column(String(20), primary_key=True)
    sex = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/shenzy')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_qqgroup = QQgroup(name='Amy', nickname='am', qq='12346', sex='女')
# 添加到session:
session.add(new_qqgroup)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
qqgroup = session.query(QQgroup).filter(QQgroup.qq=='12346').one()
# 打印类型和对象的name属性:
print('type:', type(qqgroup))
print('name:', qqgroup.name)
# 关闭Session:
session.close()
