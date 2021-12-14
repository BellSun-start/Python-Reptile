#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   抓取电影天堂信息.py
# @Time    :   2021/10/13 10:59
# @Desc    :
# 电影天堂2021必看热片， 片名， 下载地址
'''
1 提取主页面中的每一个电影后面的url
    1.拿到"2021必看热片"那一块代码（因为上下代码结构类似
    2.从刚才拿到的代码提取herf的值
2 访问子页面，提取电影名称和下载地址
    1.拿到子页面的页面源代码
    2.获取数据
'''
import requests
import re

url = "https://www.dy2018.com"
resp_rul = requests.get(url)
resp_rul.encoding = "gbk"
# gb2312,国内用的是gbk或者utf-8，就这两种
# print(resp.text)

# 提取一块html代码
obj1 = re.compile(r"2021必看热片.*?<ul>(?P<html>.*?)</ul>",re.S)
result1 = obj1.search(resp_rul.text)
html = result1.group("html")
# print(resp1.group())

# 提取herf连接的正则
obj2 = re.compile(r"<li><a href='(?P<herf>.*?)' title",re.S)
result2 = obj2.finditer(html)
# 提取电影名称和下载链接的正则
obj3 = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<movie>.*?)<br />.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">magnet',re.S)
# AttributeError: 'NoneType' object has no attribute 'group'
# movie 后面，br标签前面有个分号，提示报错没有group类型
for item2 in result2:
    # print(item2.group("herf")) # /i/104082.html
    url1 = url.strip("/") + item2.group("herf")
    # print(url1) # https://www.dy2018.com/i/104082.html
    resp_url1 = requests.get(url1)
    resp_url1.encoding = "gbk"
    # print(resp_url1.text) #打印信息正常

    result3 = obj3.search(resp_url1.text)
    movie = result3.group("movie")
    download = result3.group("download")
    print(movie,"\n",download)




