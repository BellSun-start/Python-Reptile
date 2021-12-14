
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   test.py
# @Time    :   2021/11/9 17:41
# @Desc    :
from pymysql.cursors import DictCursor
import pymysql

# 链接数据库
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='mytest'
)
# 创建游标
cursor = conn.cursor()
# 接下来就可以用游标去执行各种操作了

try:
    cursor = conn.cursor()
    result = cursor.execute("insert into stu(sname, address, gender) values ('李嘉诚', '八宝山', 1)")
    print(cursor.lastrowid)  # 获取自增的ID值
    print(result)  # result是该sql会影响多少条数据
    conn.commit()  # 提交
except:
    conn.rollback()  # 回滚