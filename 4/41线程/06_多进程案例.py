#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   06_多进程案例.py
# @Time    :   2021/11/2 16:01
# @Desc    :
# 可以使用多进程处理以下任务.
# 1.从图片网站上去抓取到图片的下载地址  -> 能办到
# 2.下载图片.  -> 能办到
import requests
from lxml import etree
from urllib.parse import urljoin
from multiprocessing import Process, Queue  # 进程之间通信

def get_all_img_src(url, q):
    resp = requests.get(url)
    resp.encoding = "utf-8"
    main_pg = resp.text
    resp.close()
    # 解析出子页面的href
    main_tree = etree.HTML(main_pg)
    li_list = main_tree.xpath("//div[@class='MeinvTuPianBox']/ul/li")
    for li in li_list:
        child_href = li.xpath("./a[1]/@href")[0]
        # print(child_href)
        # url拼接，将url和child_href进行拼接
        child_href = urljoin(url, child_href)
        # 请求到子页面. 提取子页面的页面源代码
        child_resp = requests.get(child_href)
        child_resp.encoding = "utf-8"
        child_pg = child_resp.text
        child_resp.close()

        child_tree = etree.HTML(child_pg)
        src = child_tree.xpath("//div[@class='articleV2Body re']/p/strong[@class='PicHover']/a/img/@src")
        if src:
            src = src[0]
            q.put(src)
            # print(src)
    q.put("没了") # q会一直给，给到最后没了，还会给，在给没了之后给“没了”
#
def download(q):
    while 1:
        src = q.get() # q.get()是阻塞的. 它会一直在这里拿
        if src == "没了":  # 拿到的是“没了”，就用来退出循环
            break
        # 下载图片
        img_resp = requests.get(src)
        # src="http://pic3.hn01.cn/wwl/upload/2021/09-24/x4g4dtts5uq.jpg"
        file_name = src.split("/")[-1]
        # 在当前目录下要创建imgs目录，否则会包报文件或目录找不到
        with open(f"./imgs/{file_name}", mode="wb") as f:
            f.write(img_resp.content)


if __name__ == '__main__':
    url = "http://www.591mm.com/mntt/"
    q = Queue()
    # 通过传参保障两个进程之间使用同一个队列
    p1 = Process(target=get_all_img_src, args=(url, q))
    p2 = Process(target=download, args=(q, ))
    p1.start()
    p2.start()

# 进程间数据是互不相同的，所以要利用进程间的Queue创建对象来实现通信
# 进程1和进程2 之间通过q来进程数据传递
