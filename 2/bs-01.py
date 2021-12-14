#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   bs-01.py
# @Time    :   2021/10/15 11:26
# @Desc    :
from  bs4 import BeautifulSoup
html = """
<ul>
 <li><a href="zhangwuji.com">张⽆忌</a></li>
 <li id="abc"><a href="zhouxingchi.com">周星驰</a></li>
 <li><a href="zhubajie.com">猪⼋戒</a></li>
 <li><a href="wuzetian.com">武则天</a></li>
</ul>
"""
# 初始化
page = BeautifulSoup(html, "html.parser") # html.parser使用html解析

# 常用方法find
# 使用方法： page.find("标签名", attrs={"属性":"值"}) # 查找某个元素，只会找到一个值
liabc = page.find("li",attrs={'id':'abc'})
print(liabc)
liabc_a = liabc.find("a")
print(liabc_a) # 打印a 标签
print(liabc_a.text) # 取值 周星驰
print(liabc_a.get("href")) # q取值href,用get方法

# 常用方法find_all
# 使用方法： page.find_all("标签名", attrs={"属性":"值"}) # 查找某个元素，只会找到一堆结果
li_all = page.find_all("li")
# print(li_all)
for li in li_all:
    # print(li) # 打印li标签
    li_a = li.find("a")
    # print(li_a) # 用find方法提取a标签，打印li里面的a标签
    print(li_a.text)
    print(li_a.get("href"))

