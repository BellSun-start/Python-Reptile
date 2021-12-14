#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   pyquery-01.py
# @Time    :   2021/10/21 11:11
# @Desc    :
from pyquery import PyQuery

# html="""
# <ul>
#     <li class="aaa"><a href="http://www.baidu.com">百度</a></li>
#     <li class="aaa"><a href="http://www.google.com">谷歌</a></li>
#     <li class="bbb" id="qq"><a href="http://www.qq.com">腾讯</a></li>
#     <li class="bbb"><a href="http://www.sogou.com">搜狗</a></li>
# </ul>
# """
# 添加html内容
# p = PyQuery(html)

# a = p(".aaa a") # class = "aaa"
# print(a)
# # <a href="http://www.baidu.com">百度</a><a href="http://www.google.com">谷歌</a>

# a = p("#qq a") # id= "qq"
# print(a)
# # <a href="http://www.qq.com">腾讯</a>

# href = p("#qq a").attr("href") #拿属性
# text = p("#qq a").text() #拿文本，属性值
# print(href,text)
# # http://www.qq.com 腾讯

# # 坑！！！多个标签拿属性，只能默认拿到第一个
# href = p("li a").attr("href")
# print(href)
# # # http://www.baidu.com


# it = p("li a").items()
# print(it)
# # <generator object PyQuery.items at 0x0000025375CE7DD0> # generator生成器
# for item in it:
#     href = item.attr("href")
#     text = item.text()
#     print(href,text)

# 快速总结：
# 1. PyQuery(选择器)
# 2. items()  当选择器的内容很多的时候，需要一个一个处理的时候
# 3. attr(属性名)    获取属性信息
# 4. text()   获取文本，属性值

# div = """
#     <div><span>我爱你</span></div>
# """
# p = PyQuery(div)
# html = p("div").html()  #全都要
# print(html)
# # <span>我爱你</span>
# text = p("div").text()  #只要文本，所有的html标签被过滤掉
# print(text)
# # 我爱你


# html = """
# <HTML>
#     <div class="aaa">哒哒哒</div>
#     <div class="bbb">嘟嘟嘟</div>
# </HTML>
# """
# p = PyQuery(html)

# # 在xxx标签后面添加xxxx新标签
# p("div.aaa").after("""<div class="ccc">叮叮叮</div>\n\t""")
# # <HTML>
# #     <div class="aaa">哒哒哒</div>
# #     <div class="ccc">叮叮叮</div>
# #     <div class="bbb">嘟嘟嘟</div>
# # </HTML>
# # 在xxx标签内容的后面追加标签
# p("div.aaa").append("""<span>我爱你</span>""")
# # <HTML>
# # #     <div class="aaa">哒哒哒<span>我爱你</span></div>
# # # 	<div class="bbb">嘟嘟嘟</div>
# # # </HTML>
# p("div.bbb").attr("class","aaa")                  # 修改属性（修改类标签bbb,类属性修改成aaa）
# # <HTML>
# #     <div class="aaa">哒哒哒</div>
# #     <div class="aaa">嘟嘟嘟</div>
# # </HTML>
# p("div.bbb").attr("id","123456")                  # 新增属性 （前提是标签没有照这个属性）
# # <HTML>
# #     <div class="aaa">哒哒哒</div>
# #     <div class="bbb" id="123456">嘟嘟嘟</div>
# # </HTML>
# p("div.bbb").remove_attr("id")                    # 删除属性id
# # <HTML>
# #     <div class="aaa">哒哒哒</div>
# #     <div class="bbb">嘟嘟嘟</div>
# # </HTML>
# p("div.bbb").remove()                             # 删除标签
# # < HTML >
# # < div
# #
# #
# # class ="aaa" > 哒哒哒 < / div >
# #
# # < / HTML >

# print(p)

# # 字典，无则添加，有责修改
# dic = {}
# dic['jay'] = '周杰伦'
# print(dic)
# dic['jay'] = '呵呵哒'
# print(dic)