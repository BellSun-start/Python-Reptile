#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   手刃豆瓣电影TOP250.py
# @Time    :   2021/10/12 14:55
# @Desc    :   爬取网页：https://movie.douban.com/top250
# 思路：
# 拿到页面源代码
# 编写正则，提取页面数据
# 保存文件
import requests
import re
f = open("top250.csv",mode="w",encoding="utf-8")
# csv文件是以逗号为分隔符的文件
for i in range(10):
    # print(i)
    url = f"https://movie.douban.com/top250?start={25*i}&filter="

    header ={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    # 浏览器Mozilla前面不能有空格
    res = requests.get(url, headers=header)
    Pageconnet = res.text

    #re.S 可以让正则中的.匹配换行
    obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'
                     r'导演: (?P<dao>.*?)&nbsp.*?<br>'
                     r'(?P<year>.*?)&nbsp.*?'
                     r'<span property="v:best" content="(?P<pingfen>.*?)">'
                     r'.*?<span>(?P<pingjia>.*?)人评价</span>',re.S)

    resp = obj.finditer(Pageconnet)
    for item in resp:
        name = item.group("name")
        dao = item.group("dao")
        year = item.group("year").strip()
        pingfen = item.group("pingfen")
        pingjia = item.group("pingjia")
        f.write(f"片名:{name},导演:{dao},发行年份:{year},豆瓣评分：{pingfen},评价人数：{pingjia}\n")

f.close()
res.close()
print("豆瓣top250提取完毕！")