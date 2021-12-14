#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   引题_单线程.py
# @Time    :   2021/10/27 16:21
# @Desc    :
# 单线程
def func():
    for i in range(2):
        print(i)

# main 回车就可以。可以把这个当做程序的入口
if __name__ == '__main__':
    print("第1遍")
    func()
    print("第2遍")
    func()