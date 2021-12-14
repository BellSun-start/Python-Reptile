# 可以使用多进程处理以下任务.
# 1.从图片网站上去抓取到图片的下载地址  -> 能办到
# 2.下载图片.  -> 能办到

# http://pic3.hn01.cn/wwl/upload/2021/09-27/urnui3zx1mn.jpg

import requests
from lxml import etree
from multiprocessing import Process, Queue  # 进程之间通信
from urllib.parse import urljoin


def get_all_img_src(url, q):
    resp = requests.get(url)
    resp.encoding = "utf-8"
    main_pg = resp.text
    resp.close()  # 关掉链接
    # 解析出子页面的href
    main_tree = etree.HTML(main_pg)
    li_list = main_tree.xpath("//div[@class='MeinvTuPianBox']/ul/li")
    for li in li_list:
        child_href = li.xpath("./a[1]/@href")[0]
        # 拼接url地址
        # urljoin拼接的地址是不用考虑/在前, 还是在后的
        child_href = urljoin(url, child_href)
        # 请求到子页面. 提取子页面的页面源代码
        child_resp = requests.get(child_href)
        child_resp.encoding = 'utf-8'
        child_pg = child_resp.text
        child_resp.close()

        child_tree = etree.HTML(child_pg)
        src = child_tree.xpath("//img[@id='mouse_src']/@src")
        if src:
            src = src[0]
            q.put(src)  # 把src塞入队列,  有可能会停
    q.put("没了")


def download_img(q):
    while 1:
        src = q.get()  # q.get()是阻塞的. 它会一直在这里拿
        if src == '没了':
            break
        # 下载图片的逻辑
        img_resp = requests.get(src)
        # src="http://pic3.hn01.cn/wwl/upload/2021/09-24/x4g4dtts5uq.jpg"
        file_name = src.split("/")[-1]
        with open(f"./imgs/{file_name}", mode="wb") as f:
            f.write(img_resp.content)


if __name__ == '__main__':
    url = "http://www.591mm.com/mntt/"
    q = Queue()
    # 通过传参保障两个进程之间使用同一个队列
    p1 = Process(target=get_all_img_src, args=(url, q))
    p2 = Process(target=download_img, args=(q, ))
    p1.start()
    p2.start()
