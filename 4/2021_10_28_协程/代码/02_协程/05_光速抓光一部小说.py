import requests
from lxml import etree
import asyncio
import aiohttp
import aiofiles
import os


def get_chapter_info(url):
    # 1. 获取到主页面的内容. 并将数据整理成一个超大号的列表.
    """
    返回
    [
        {chapter_name:title, chapter_href:[1.html, 2.html......]},
        {},
        {},
        {},
        {},
    ]
    """
    resp = requests.get(url)
    resp.encoding = "utf-8"  # 记住这里. 一会儿有用
    page_source = resp.text
    resp.close()  # 关闭链接

    result = []

    # 解析
    tree = etree.HTML(page_source)
    tables = tree.xpath("//div[@class='mulu']/center/table")
    for tab in tables:
        chapter = {}
        trs = tab.xpath("./tr")
        title = trs[0].xpath(".//text()")
        chapter_name = "".join(title).strip()

        chapter_hrefs = []
        for tr in trs[1:]:  # 从第二行开始获取每一个小节的href
            hrefs = tr.xpath("./td/a/@href")
            chapter_hrefs.extend(hrefs)
        chapter['chapter_name'] = chapter_name
        chapter['chapter_hrefs'] = chapter_hrefs

        result.append(chapter)
    return result


async def download_one(name, href):
    # 1.创建session
    # 2.发送请求
    # 3.从响应中获取到页面源代码
    async with aiohttp.ClientSession() as session:
        async with session.get(href) as resp:
            page_source = await resp.text(encoding='utf-8')  # resp.encoding = "xxxx"
            # 4.解析页面源代码. 拿到文件名称以及小说的内容
            # 5.写入文件
            tree = etree.HTML(page_source)
            file_name = tree.xpath("//div[@class='main']/h1/text()")[0].strip()
            content = "\n".join(tree.xpath("//div[@class='content']/p//text()"))  # <p> 段落. 有换行的作用

            async with aiofiles.open(f"{name}/{file_name}.txt", mode="w", encoding="utf-8") as f:
                await f.write(content)

    print(file_name, "下载完成!")


async def download_chapter(name, hrefs):
    # 1. 创建文件夹
    if not os.path.exists(name):  # 判断是否有这个文件
        os.makedirs(name)  # 创建文件夹
    # 2. 给这一堆链接分配任务
    tasks = []
    for href in hrefs:
        # 创建任务
        t = asyncio.create_task(download_one(name, href))
        tasks.append(t)
    await asyncio.wait(tasks)


async def download_all(all_chapter):
    tasks = []
    for chapter in all_chapter:
        name = chapter['chapter_name']
        if not os.path.exists(name):
            os.makedirs(name)
        hrefs = chapter['chapter_hrefs']
        for href in hrefs:  # 拿到每一个连接
            t = asyncio.create_task(download_one(name, href))
            tasks.append(t)
    await asyncio.wait(tasks)


def main():
    url = "http://www.mingchaonaxieshier.com/"
    # 1. 获取到章节信息
    chapter_info = get_chapter_info(url)  # [{},{},{}]
    # 2. 开始异步下载了
    # # 方案一. 一个章节一个章节下载
    # for chapter in chapter_info:
    #     chapter_hrefs = chapter['chapter_hrefs']
    #     chapter_name = chapter['chapter_name']
    #     # 开始批量下载
    #     asyncio.run(download_chapter(chapter_name, chapter_hrefs))

    # 方案二. 一起下载
    asyncio.run(download_all(chapter_info))


if __name__ == '__main__':
    main()
    # lst = [1,2,3]
    # lst2 = [4,5,6]
    # lst.extend(lst2)
    # print(lst)


# 不是所有的网站和需求都可以上协程的.
# 有些网站反爬非常的厉害. 一般不用协程. 这种网站一般越慢越好.
