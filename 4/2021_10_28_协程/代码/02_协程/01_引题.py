
def func():
    print("开始准备抓取xxx网站")  # 1s => 1000W
    # 开始进行数据抓取
    # requests.get(百度)  # 0.01s  站在cpu的角度来说. 这里并没有充分的利用到CPU的资源
    # 文件的读写  也不能充分的利用到cpu资源, CPU最喜欢最适合的是运算
    print("保存数据")
    # 目前我们写的多线程程序由于里面有大量的网络请求, 所以, 目前没办法充分的利用到CPU资源

    # 银行柜台(CPU): 李四, 王二麻子
    # 张三 回家


if __name__ == '__main__':
    # t = Thread(target = func)
    # t = Thread(target = func)
    # t = Thread(target = func)
    func()


# 协程: 让单个线程可以同时运行多个任务. 那么每个任务在执行的时候会遇到IO操作. 遇到IO就挂起, 切换到其他的任务上. 等待IO的结束后, 再继续执行任务
# IO操作: 网络请求. 文件读写
