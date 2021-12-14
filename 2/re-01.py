#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   re-01.py
# @Time    :   2021/10/11 15:45
# @Desc    :
import re
# # findall 查找所有，返回list
# lst = re.findall("m","tom cat tell me,  you will eat the tom, tom is too small!")
# print(lst)  # ['m', 'm', 'm', 'm', 'm']
# lst = re.findall(r"\d+", "预计5年内能考取山东大学工程管理的前500名")
# print(lst)  # ['5', '500']

# finditer 返回的是迭代器，重点！iterator迭代器
# #----------------------------------------------------------------
result = re.finditer(r"\d+","我今年26岁，定个小目标，挣他1一个亿")
# print(result) # <callable_iterator object at 0x000001CC345EB340>
for item in result: # 通过循环从迭代器中取东西
    # print(item)
    # < re.Match object;span = (3, 5), match = '26' > Match:匹配
    # < re.Match object;span = (15, 16), match = '1' >
    print(item.group()) # 从匹配到的结果，拿到数据
    # 26
    # 1
# #----------------------------------------------------------------

# # search 匹配到第一个结果就返回，没有匹配到返回None
# lst_se = re.search(r"\d", "小明在2010年的时候穿越到了2022年！")
# print(lst_se.group()) #2
#
# # # match 只能从字符串的开头进行匹配,类似在正则前面加了^
# res_ma = re.match('a','abcd').group()
# print(res_ma) #a
#
# # 预加载，提前把正则对象加载完成
# obj = re.compile(r"\d+")
# # 直接把加载好的正则进行使用
# res = obj.findall("我叫爸爸，今年26岁，我的大学是在2008年毕业的")
# print(res) # ['26', '2008']
#
