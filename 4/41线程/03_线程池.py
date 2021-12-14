#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   03_线程池.py
# @Time    :   2021/10/28 16:56
# @Desc    :
# 100个任务. 能不能创建100个线程
# A, 能
# B, 不能
# 线程不是越多越好.

from  concurrent.futures import ThreadPoolExecutor
# 1.单个任务，去下载图片
def download(name):
    # print("我要去下载图片")
    for i in range(20):
        print(name, i)
    # print("我要去下载图片", name)
# 2.可以使用线程池来管理线程和任务之间的关系
if __name__ == '__main__':
    # 4 准备线程池
    # 线程池中线程个数是2；同时运行的任务上限；有with 可以自动关闭任务，和with open类似
    with ThreadPoolExecutor(2) as t:
        # # 给线程池提交任务的第一种逻辑
        # # 3.准备好10个任务 #["a","b","c","d","e"]使用字母显示更方便
        # for i in range(10):
        #         job = f"任务{i}"   # 任务0，任务1...
        #         # Thread(target=xxx,args=xxx)
        #         # 提交任务
        #         # 第一个参数：干什么，任务（单任务）
        #         # 后面的参数：执行任务需要提交的信息
        #         # 可以包含多个提交的信息
        #         # 此地将job传给download的name中去
        #         t.submit(download, job)

        # # 给线程池提交任务的第二种逻辑
        # t.map(发钱，10个人的名字)
        t.map(download,(f"任务{i}" for i in range(10)))
    print("我是主进程")

