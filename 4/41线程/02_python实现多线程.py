#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   02_python实现多线程.py
# @Time    :   2021/10/28 10:39
# @Desc    :

# 2.导入需要用到的包
from threading import Thread
#
# # 1.定好任务
# def func():
#     for i in range(10):
#         print("我的任务是", i)
#
# # 3.编写main，主线程
# if __name__ == '__main__':
#     # 4。创建一个线程
#     # 创建的线程不会默认执行，要用target进行调度，调度任务func,不要加()
#     t = Thread(target=func) #target是任务
#     # 调度任务去执行，这里是线程开始的地方
#     t.start()
#     for j in range(10):
#         print("我是店长", j)

# 多线程的第一种写法
def func(name):
    # 想象，这里是消灾图片的代码
    for i in range(10):
        print(name, i)
if __name__ == '__main__':
    # 要用target进行调度
    # args进行传参，传给name。
    # 要求传过去的必须是元素，只有一个元素的话，必须加', '
    t1 = Thread(target=func, args=("樵夫",))
    t2 = Thread(target=func, args=("佩奇",))
    t1.start()
    t2.start()

# # 多线程的第二种写法.  面向对象的写法（不用管）
# class MyThread(Thread):  # 这玩意可以创建子线程
#
#     def __init__(self, name):  # self就是当前这个对象
#         # 这句话固定
#         super(MyThread, self).__init__()
#         # print("特意标记一下", name)
#         # print(self)
#         self.name = name
#
#
#     def run(self):  # run就是任务
#         print("我是run里面", self.name)
#         # for i in range(1000):
#         #     print('子线程', i)
#
#
# if __name__ == '__main__':
#     t1 = MyThread("alex")  # 直接创建出来了一个子线程
#     print(t1)
#     t1.start()  # 线程开始运行  ->  这里面会自动的让子线程去执行里面的run()这个功能
#
#     t2 = MyThread("wusir")  # 直接创建出来了一个子线程
#     t2.start()
#     # for j in range(999):
#     #     print("我是主线程", j)