#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   数据筛选_改值为123456789.py
# @Time    :   2021/10/8 17:55
# @Desc    :
# from urllib.request import urlopen
#
# url = "https://hao.360.com/"
#
# resp = urlopen(url)
#
# # print(resp.read().decode("utf-8"))
# with open("360.html",encoding="utf-8",mode="w") as f:
#     f.write(resp.read().decode("utf-8"))

from urllib.request import urlopen

url = "http://www.baidu.com"

resp = urlopen(url)

# print(resp.read().decode("utf-8"))
with open("baidu.html",encoding="utf-8",mode="w") as f:
    f.write(resp.read().decode("utf-8"))