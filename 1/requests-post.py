#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   requests-post.py
# @Time    :   2021/10/9 16:35
# @Desc    :
import  requests

url = "https://fanyi.baidu.com/sug"

shuju = {
    "kw": input("请输入一个单词：")
}

resp = requests.post(url,data=shuju)

# 拿到的是文本字符串
# print(resp.text)
# 拿到的是json数据
print(resp.json())
print(resp.json()['errno'])
print(resp.json()['data'][3]['v'])
