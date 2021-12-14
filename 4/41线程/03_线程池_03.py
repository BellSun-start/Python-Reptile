#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   03_线程池_03.py
# @Time    :   2021/11/1 14:54
# @Desc    :
from concurrent.futures import ThreadPoolExecutor

def main(name):
    for i in range(1000):
        print(name,i)

# 线程池
if __name__ == '__main__':
    with ThreadPoolExecutor(10) as t:
        for i in ["1a","2b","3c","4d","5e","6f","7g","8h"]:
            t.submit(main,f"任务{i}是：")