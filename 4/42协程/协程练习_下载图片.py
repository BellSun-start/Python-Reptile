#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author:玄铁重剑无锋
# @Author  :   {玄铁重剑无锋}
# @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# @Contact :   {sfrexpect@163.com}
# @File    :   协程练习_下载图片.py
# @Time    :   2021/11/3 10:26
# @Desc    :

import asyncio
# # python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple aiohttp
import aiohttp  # 也可以进行网络请求. 和requests区别. 它里面支持异步协程
# # python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple aiofiles
import aiofiles

# 下载图盘的任务
# 如果里面是协程函数，外面没有加async，则会报错
async def download(url):
    file_name = url.split("/")[-1]
    # print(file_name)
    # 1.创建session对象
    # 2.发送请求
    # 3.读取文件
    # 4.协程写数据
    print("开始下载",url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.content.read() # 图片视频要用content获得内容，并用read()读取
            async with aiofiles.open(file_name, mode="wb") as f: # 协程，自动关闭
                await f.write(content) # 写不可能一次写完，要进行挂起
    print("下载成功")



async def main():
    url_list = [
        "https://x.u5w.cc/Uploadfile/202110/20/42214426253.jpg",
        "https://x.u5w.cc/Uploadfile/202110/20/B3214426373.jpg",
        "https://www.xiurenji.vip/uploadfile/202110/20/1F214426892.jpg",
        "https://www.xiurenji.vip/uploadfile/202110/20/91214426753.jpg"
    ]
    tasks = []
    for url in url_list:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    # 等待所有任务结束,如果没有等待所有任务结束，就会出现图片不下载的情况
    # 重要易出错地点
    await asyncio.wait(tasks)

if __name__ == '__main__':
    # # 方案一
    m = main()
    # # 2. 想要运行协程对象必须要有一个超大号的event_loop -> 事件循环
    event_loop = asyncio.get_event_loop()
    # # 3. 用event_loop运行协程对象. 让协程对象中的任务可以执行, 等待执行完毕
    event_loop.run_until_complete(m)
    # # 方案二：
    # asyncio.run(main())# 如果是windows的同学要注意. 这句话里面会有事件循环的关闭操作, 容易和windows的事件管理相冲突.
    # 如果你的电脑运行这句话出现了. RuntimeError: Event loop is closed ->  请更换为方案一即可