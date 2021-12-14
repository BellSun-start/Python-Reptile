#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   防盗链视频处理.py
# @Time    :   2021/10/26 16:13
# @Desc    :
# 原始网页：
# https://www.pearvideo.com/video_1744457
# Request URL:
# https://www.pearvideo.com/videoStatus.jsp?contId=1744457&mrd=0.8432471833659037
# srcUrl: " "
# https://video.pearvideo.com/mp4/adshort/20211025/1635235696458-15787334_adpkg-ad_hd.mp4
# 视频地址：
# https://video.pearvideo.com/mp4/adshort/20211025/cont-1744457-15787334_adpkg-ad_hd.mp4
# 视频地址和原始网页，以及srcUrl产生的联系是在contID，也就是1744457
# 1、拿到contID
# 2、拿到videoStatus返回的json -> srcUrl
# 3、srcUrl里面的内容进行修整
# 4、下载视频
import requests
url = "https://www.pearvideo.com/video_1744457"
contID = url.split("_")[1] # 以_为分隔符，获得1744457
video_url = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.8432471833659037"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    # 防盗链，上一级是谁
    "Referer": "https://www.pearvideo.com/video_1744457"
}
resp = requests.get(video_url,headers=headers)
# print(resp.json()) # 就是Preview里面的数据
dic = resp.json()
systemTime = dic['systemTime']
# print(systemTime)
fault_video_url = dic['videoInfo']['videos']['srcUrl']
# print(fault_video_url)
# true_video_url = fault_video_url.replace(systemTime,'cont-'+contID) #拼接成真正的url地址
true_video_url = fault_video_url.replace(systemTime,f"cont-{contID}")
# print(true_video_url)

# 下载视频
# with open("a.mp4", mode="wb") as f:
with open(f"{contID}.mp4", mode="wb") as f:
    f.write(requests.get(true_video_url).content) #最后的content,得到的视频的内容，写入到文件中去
