#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   requests-01.py
# @Time    :   2021/10/9 13:11
# @Desc    :
import requests
url = "http://www.baidu.com"
resp = requests.get(url)
resp.encoding = "utf-8"
print(resp.text)
with open("baidu-request.html",mode="w",encoding="utf-8") as f:
    f.write(resp.text)