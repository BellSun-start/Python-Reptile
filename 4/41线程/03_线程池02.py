#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   03_线程池02.py
# @Time    :   2021/10/29 16:34
# @Desc    :
from concurrent.futures import ThreadPoolExecutor
import time

def func(name):
    time.sleep(1)
    return name


def do_callback(res):
    print(res.result())


if __name__ == '__main__':
    start_0 = time.time()
    with ThreadPoolExecutor(10) as t:
        names = ["线程1", "线程2", "线程3"]
        for name in names:
            # 方案一, 添加回调
            t.submit(func, name).add_done_callback(do_callback)
    print(time.time() - start_0)
if __name__ == '__main__':
    start = time.time()
    with ThreadPoolExecutor(10) as t:
        names = [5, 13, 3]
        # 方案二, 直接用map进行任务分发. 最后统一返回结果
        results = t.map(func, names, )  # 结果是按照你传递的顺序来执行的, 代价就是如果第一个没结束. 后面就都没结果
        for r in results:
            print("result", r)
    print(time.time() - start)