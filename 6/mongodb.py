#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   mongodb.py
# @Time    :   2021/11/11 15:23
# @Desc    :
import requests
from lxml import etree
import mongodb
from concurrent.futures import ThreadPoolExecutor


def get_page_source(url):
    resp = requests.get(url)
    page_source = resp.text
    return page_source


def parse_html(html):
    tree = etree.HTML(html)
    # print(html)
    li_list = tree.xpath("//ul[@class='sellListContent']/li")
    print("==>", len(li_list))
    try:
        lst = []
        for li in li_list:
            title = li.xpath("./div[1]/div[1]/a/text()")[0]
            position_info = "-".join((s.strip() for s in li.xpath("./div[1]/div[2]/div/a/text()")))

            temp = li.xpath("./div[1]/div[3]/div/text()")[0].split(" | ")
            if len(temp) == 6:
                temp.insert(5, "")
            elif len(temp) == 8:
                temp.pop()
            huxing, mianji, chaoxiang, zhangxiu, louceng, nianfen, jiegou = temp
            guanzhu, fabushijian = li.xpath("./div[1]/div[4]/text()")[0].split(" / ")
            tags = li.xpath("./div[1]/div[5]/span/text()")

            data = {
                "title": title,
                "position": position_info,
                "huxing": huxing,
                "mianji": mianji,
                "chaoxiang": chaoxiang,
                "zhangxiu": zhangxiu,
                "louceng": louceng,
                "nianfen": nianfen,
                "jiegou": jiegou,
                "guanzhu": guanzhu,
                "fabushijian": fabushijian,
                "tags": tags
            }
            lst.append(data)
        # 一起存入mongodb
        print(f"数据量", len(lst))
        result = mongodb.add_many("ershoufang", lst)
        print(f"插入{len(result)}")
    except Exception as e:
        print(e)
        print(temp)

def main(url):
    page_source = get_page_source(url)
    parse_html(page_source)


if __name__ == '__main__':
    with ThreadPoolExecutor(10) as t:
        for i in range(1, 31):
            url = f"https://bj.lianjia.com/ershoufang/pg{i}/"
            t.submit(main, url)

