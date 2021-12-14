#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   cookie_处理.py
# @Time    :   2021/10/25 16:34
# @Desc    :
import  requests
session = requests.session()
data = {
    "loginName": "17853946102",
    "password": "123sfr"
}
# # 1.登陆
# # 从登陆界面拿到有session，使下面的会话能继续使用session的信息
# url = "https://passport.17k.com/ck/user/login"
# resp1 = session.post(url,data=data)
# print(resp1.text, "\n")
# print(resp1.cookies)
# # 2.拿书架上的数据
# # https://user.17k.com/www/bookshelf/index.html
# # 刚才的session中是有cookie的
# # https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919
# # url ?后面的内容是没有用的
# resp2 = session.get("https://user.17k.com/ck/author/shelf")
# # print(resp2.text)
# print(resp2.json())

# resp = requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
# print(resp.text)
# # {"status":{"code":10103,"msg":"用户登陆信息错误"},"time":1635219137000}

resp = requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919", headers={
    "Cookie": "GUID=593eb0a6-9d53-40e3-83d0-8780304b87c8; c_channel=0; c_csc=0; BAIDU_SSP_lcr=https://www.baidu.com/link?url=zSY9FO7mPM9Rj6YuqDn8fXhhAPpnnpizNtLHwPyrtx3&wd=&eqid=8e2df48d0000ddc7000000066177742a; Hm_lvt_9793f42b498361373512340937deb2a0=1635141983,1635143390,1635143635,1635218482; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%226807569%22%2C%22%24device_id%22%3A%2217cb60e3ecc92e-0c4f5f2386794e-c343365-2073600-17cb60e3ecdb1f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22593eb0a6-9d53-40e3-83d0-8780304b87c8%22%7D; accessToken=avatarUrl%3Duser%252Favatar%252F09%252F69%252F75%252F6807569.jpg-88x88%253Fv%253D1560442721000%26id%3D6807569%26nickname%3D%25E5%258D%2583%25E4%25BA%25BF%25E5%25B0%2591%25E5%25A5%25B3%25E6%25A2%25A688%26e%3D1650770548%26s%3Df5f9034ef18675d3; Hm_lpvt_9793f42b498361373512340937deb2a0=1635218565"
})
print(resp.text)
print(resp.json())
