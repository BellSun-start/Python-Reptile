#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   汽车之家A8评测.py
# @Time    :   2021/10/22 10:52
# @Desc    :
'''
1.提取页面源代码
2.解析页面源代码，提取数据
'''
import requests
from pyquery import PyQuery

f = open("奥迪A8.csv", mode="w", encoding='utf-8')
def get_page_source(url):
    resp = requests.get(url)
    resp.encoding = "gbk"
    # print(resp.text)
    return resp.text
    # # pass
    # # return 应该产生返回值

def parse_page_source(html):
    doc =PyQuery(html)
    # choose-con 和 mt-10 是两个class  你那个写法 应该是提取 .choose-con 下的 mt-10
    # class = "choose-con mt-10"使用.choose-con.mt-10进行提取
    mydata_list = doc(".mt-10").items() # 返回结果多，需要用选择器
    for mydata in mydata_list:
        # 符合div dl dd的内容有很多
        # 在css进行选择的时候，获取第一个位置用:nth-child(1)
        # 在已经提取的内容中，获取第一个用 .eq(0)
        if not mydata("div > dl:nth-child(3) > dt:contains('购车经销商')"):
            mydata("div > dl:nth-child(2)").after(PyQuery("""<dl class="choose-dl">
                        <dt>购车经销商</dt>
                        <dd>
                            <a href="###" class="js-dearname" data-val='2080705,47761' data-evalid="3489419" target="_blank">
                                &nbsp
                            </a>
                        </dd>
                    </dl>"""))

        chexing = mydata("div > dl:nth-child(1) > dd").eq(0).text().replace("\n", "").replace(" ","")
        address = mydata("div > dl:nth-child(2) > dd").text()
        buy_date = mydata("div > dl:nth-child(4) > dd").text()
        # print(type(mydata("div > dl:nth-child(1)"))) #确定代码的类型为PyQuery类型 <class 'pyquery.pyquery.PyQuery'>
        price = mydata("div > dl:nth-child(5) > dd").text()
        youhao = mydata("div > dl:nth-child(6) > dd > p").eq(0).text().replace(" 升/百公里", "")
        gongli = mydata("div > dl:nth-child(6) > dd > p").eq(1).text().replace(" 公里", "")
        pingjia = mydata("div > div > dl > dd").text().split()
        f.write(f"{chexing},{address},{buy_date},{price},{youhao},{gongli},{','.join(pingjia)}\n")
        # print(pingjia)
    # # pass

# f.close()
def main():
    url = "https://k.autohome.com.cn/146/"
    # 1.提取页面源代码
    html = get_page_source(url)
    # print(html)
    # 2.解析页面源代码，提取数据
    parse_page_source(html)

if __name__ == '__main__':
    main()