#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   requests-get.py
# @Time    :   2021/10/9 13:28
# @Desc    :
import requests
# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
connet = input("Please input your search :")

## 百度的直接用浏览器就可以爬取到数据
# url = f"http://www.baidu.com/s?wd={connet}"
#

# 搜狗的浏览器需要用到反扒，添加浏览器标识
url = f"https://www.sogou.com/web?query={connet}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
resp = requests.get(url,headers = headers)


# print(resp.text)
# 查看请求头信息，百度的请求头用软件就可以访问，搜狗的请求头不能使用软件
# print(resp.request.headers)

with open("request-get-sogou.html",mode="w",encoding="utf-8") as f:
    f.write(resp.text)