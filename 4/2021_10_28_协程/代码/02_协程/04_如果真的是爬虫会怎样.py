import asyncio
import requests
import aiohttp  # 也可以进行网络请求. 和requests区别. 它里面支持异步协程  pip install aiohttp
import aiofiles  # pip install aiofiles

# 下载图片的任务
async def download(url):
    file_name = url.split("/")[-1]
    print("我要开始下载了", url)
    # 用法:1.创建一个session对象
    # with open(xxx) as f:
    async with aiohttp.ClientSession() as session:  # 相当于requests.session()
        # 发送网络请求,
        async with session.get(url) as resp:  # resp = session.get()  resp.text
            # content = await resp.text()  # text() 获取文本  # 这里必须挂起   A 能,. B, 不能
            content = await resp.content.read()  # 如果获取的是二进制字节, 需要用read()  # 这里必须挂起   A 能,. B, 不能

            # # 存储到硬盘上,  open是线程同步的代码. 它是不会任务切换的. 但是在携程函数内是可以使用的.  但是效率低
            # with open(file_name, mode="wb") as f:
            #     f.write(content)
            async with aiofiles.open(file_name, mode="wb") as f:
                await f.write(content)  # 要挂起

    print("下载成功")


async def main():
    # 想办法从网站里面拿到一堆的图片的url地址
    url_list = [
        "https://x.u5w.cc/Uploadfile/202110/20/42214426253.jpg",
        "https://x.u5w.cc/Uploadfile/202110/20/B3214426373.jpg",
        "https://www.xiurenji.vip/uploadfile/202110/20/1F214426892.jpg",
        "https://www.xiurenji.vip/uploadfile/202110/20/91214426753.jpg"
    ]
    tasks = []
    for url in url_list:
        t = asyncio.create_task(download(url))  # 创建好一个任务. 任务里面是一个协程对象. 该协程对象指向的是某一个url
        tasks.append(t)
    # 等待所有下载任务结束
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # asyncio.run(main())
    m = main()
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(m)