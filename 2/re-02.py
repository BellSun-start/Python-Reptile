#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   re-02.py
# @Time    :   2021/10/12 14:03
# @Desc    :
import re
import requests
# s='''
# <div class='⻄游记'><span id='10010'>中国联通</span></div>
# <div class='水浒传'><span id='10086'>中国移动</span></div>
# '''
# obj = re.compile("<span id='(?P<id>\d+)'>(?P<name>.*?)</span>")
# res = obj.finditer(s)
#
# for i in res:
#     id = i.group("id")
#     print(id)
#     name = i.group("name")
#     print(name)



####### 可删除
with open("./test.txt", mode="r", encoding="UTF-8") as f1:
    # print(type(f1))
    # print(f1.read())
    obj = re.compile(r"<HEAD>(?P<key>.*?)</HEAD>",re.S)
    resp = obj.finditer(f1.read())
    for item in resp:
        print(item.group("key"))

