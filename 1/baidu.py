# -*- coding:utf-8 -*-
# @Time : 2021/8/20 9:36
# @Author: 玄铁重剑无锋
# @File : baidu.py
from urllib.request import urlopen
# urllib库里面有个request模块 有个函数urlopen

url = "http://www.baidu.com"

resp = urlopen(url)

# print(resp)
# 看不到内容，需要用read给读出来

# print(resp.read())
# 获得b开头的字节，需要用decode进行解码
# ctrl + f 搜索charset，两种情况utf-8和gbk

print(resp.read().decode("utf-8"))
# 此时拿到的是页面源代码