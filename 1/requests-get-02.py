#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   requests-get-02.py
# @Time    :   2021/10/11 10:07
# @Desc    :
import requests
# url 只存放？之前的地址，？之后的都涉及数据,需要在网页中“Query String Parameters”单独获得
url = "https://movie.douban.com/j/chart/top_list"

shuju = {
    "type": "13",
    "interval_id": "100:90",
    "action":"",
    "start": "0",
    "limit": "20"
}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

resp = requests.get(url, params=shuju,headers=headers)

print(resp.text)
print(resp.json())