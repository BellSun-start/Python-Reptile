#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   04中国历年电影票房.py
# @Time    :   2021/10/29 17:48
# @Desc    :
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
# http://www.boxofficecn.com/boxofficecn

def get_page_source(url):
    resp = requests.get(url)
    resp.encoding = "utf-8"
    pg = resp.text
    resp.close()
    return pg


def parse_data(html):
    try: # 尝试执行代码
        tree = etree.HTML(html) # 把页面源代码加载进来
        tr_list = tree.xpath("//table/tbody/tr")[1:] # 表头的信息是有问题的，所以去掉表头
        for tr in tr_list:
            # xpath默认情况拿到的是列表
            year = tr.xpath("./td[2]//text()")[0]   # 防止有span之类的标签，要的是子子孙孙的数据
            name = tr.xpath("./td[3]//text()")[0]
            money = tr.xpath("./td[4]//text()")[0]
            # print(type(money))
            # print((year, name, money)) # 打印的是元组
            # 元组的方式提取数据
            # f.write(",".join((year, name, money)))
            # 字符拼接的方式写入数据
            f.write(f"{year}, {name}, {money}\n")
            # 执行的时候发现有报错
            # 因为一些行存在没有这三个数据
    except Exception as e:  # =如果报错的时候就走这里，不报错就不走这里
        print(e, "打印 error")


def main(url):
    # 1.得到源码
    # # url = "http://www.boxofficecn.com/boxoffice2020"
    # 将函数返回值pg给了page_source
    page_source = get_page_source(url)
    # 2.解析数据,直接下载图片
    parse_data(page_source)



if __name__ == '__main__':
    with open("data.csv", mode="w", encoding="utf-8") as f:
    # f = open("data.csv", mode="w", encoding="utf-8")
        # 获取所有任务的网址，这是全部的任务
        url_list = []
        for i in range(1994, 2022):
            url_list.append(f"http://www.boxofficecn.com/boxoffice{i}")
        # 单线程
        # for url in url_list:
        #         main(url)
        # 线程池
        with ThreadPoolExecutor(5) as t:
            for url in url_list:
                t.submit(main, url)
# 1. 先写不用多线程的时候. 如何进行抓取
# 2. 尝试找到那个不同任务之间的区别(url)
# 3. 改写成一个多线程的逻辑即可




