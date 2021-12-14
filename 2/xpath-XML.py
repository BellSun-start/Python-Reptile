#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   xpath-XML.py
# @Time    :   2021/10/20 10:23
# @Desc    :
from lxml import etree
# 两种导入方式是一样的
# from lxml import html
# etree = html.etree

# book/*/nick 此行代码出现在xml中会报错，间接提示代码一定要干净
xml = """
<book>
	<id>1</id>
	<name>野花遍地⾹</name>
	<price>1.23</price>
	<nick>臭⾖腐</nick>
		<author>
			<nick id="10086">周⼤强</nick>
			<nick id="10010">周芷若</nick>
			<nick class="jay">周杰伦</nick>
			<nick class="jolin">蔡依林</nick>
			<div>
				<nick>惹了</nick>
			</div>
		</author>
	<partner>
		<nick id="ppc">胖胖陈</nick>
		<nick id="ppbc">胖胖不陈</nick>
	</partner>
</book>
"""
# 此时练习只用xml
et = etree.XML(xml)
# result = et.xpath("/book")                    #/表示根节点
# result = et.xpath("/book/name")               # 在xpath中间的/表示是儿子（或者是里面的）
# result = et.xpath("/book/name/text()")        # 拿出来name里面的文本列表
# result = et.xpath("/book/name/text()")[0]     # 拿出来name里面的文本
# result = et.xpath("/book//nick/text()")       # 7个 拿出来的是book的子子孙孙所有的nick的文本列表
# result = et.xpath("/book/*/nick/text()")      # 6个 拿出来的是book的孙子辈分的nick的文本列表
# *通配符，谁都行
# result = et.xpath("/book/author/nick[@class='jay']/text()")
# []表示属性筛选，@属性名=值 同find方法类似  page.find("标签名", attrs={"属性":"值"})
# result = et.xpath("/book/partner/nick/@id")     # 最后一个/表示拿到里面的内容，@属性，可以直接拿到属性值
# print(result)
