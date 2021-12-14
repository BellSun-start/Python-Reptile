import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


def get_page_source(url):
    resp = requests.get(url)
    resp.encoding = "utf-8"
    pg = resp.text
    resp.close()  # 关闭链接
    return pg


def parse_data(html):

    try:  # 尝试执行代码
        tree = etree.HTML(html)  # 把页面源代码加载进来
        tr_list = tree.xpath("//table/tbody/tr")[1:]  # 表头是不要的
        for tr in tr_list:
            # 这里面有bug. 需要各位自行去修正这个bug
            year = tr.xpath("./td[2]//text()")[0]  # xpath默认情况下拿到的数据是列表
            name = tr.xpath("./td[3]//text()")[0]
            money = tr.xpath("./td[4]//text()")[0]

            # print(year, name, money)
            # f.write(f"{year},{name},{money}")
            f.write(",".join((year, name, money)))
            f.write("\n")
    except Exception as e:  # 如果报错. 就走这里. 不报错就不走这里
        print(e)


def main(url):
    # 获取页面源代码
    page_source = get_page_source(url)
    # 解析数据, 解析完的数据直接存储到文件中
    parse_data(page_source)


if __name__ == '__main__':
    f = open("data.csv", mode="w", encoding="utf-8")
    lst = []
    for i in range(1994, 2022):
        lst.append(f"http://www.boxofficecn.com/boxoffice{i}")


    # # 单线程的逻辑
    # for url in lst:
    #     main(url)

    # 线程池逻辑
    with ThreadPoolExecutor(5) as t:
        for url in lst:
            t.submit(main, url)

# 1. 先写不用多线程的时候. 如何进行抓取
# 2. 尝试找到那个不同任务之间的区别(url)
# 3. 改写成一个多线程的逻辑即可
