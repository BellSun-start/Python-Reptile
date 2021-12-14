from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor
# from concurrent.futures import ThreadPoolExecutor
# from threading import Thread


def func():
    for i in range(1000):
        print("我是子进程", i)


if __name__ == '__main__':
    # 1.创建子进程
    p = Process(target=func, args=())
    # 2.启动这个进程
    p.start()
    for i in range(1000):
        print("我是主进程", i)


class MyProcss(Process):
    def run(self):
        for j in range(999):
            print("子进程", 999)


if __name__ == '__main__':
    p1 = MyProcss()
    p1.start()
    with ProcessPoolExecutor(10) as p:
        p.submit()

# 多线程, 任务之间的相似度很高.
# 多进程, 任务与任务之间相似度很低. 关联性也相对较低
