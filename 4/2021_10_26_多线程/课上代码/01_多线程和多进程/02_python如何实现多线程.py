# 2. 引入多线程需要用到的包
from threading import Thread  # 线程
# 第一种创建多线程的逻辑
# # 1. 定好任务
# def func():
#     # 想像. 这里是下载图片的代码
#     for i in range(1000):
#         print("我的任务是", i)
#
#
# # 3. 编写main
# if __name__ == '__main__':
#     # 4. 创建一个线程
#     # 创建出来的线程不会默认直接就执行
#     t = Thread(target=func)  # target 任务
#     # 5. 调度线程去执行
#     t.start()  # 在这里才是真正的告诉线程可以开始执行了
#
#     # 主线程应该可以继续往下走才对
#     for j in range(1000):
#         print("我是店长", j)


def func(name):
    # 想像. 这里是下载图片的代码
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    func("你好啊")
    t1 = Thread(target=func, args=("樵夫",))
    t2 = Thread(target=func, args=("沛齐",))
    t1.start()
    t2.start()
    # 该怎么办还继续怎么办.. 没人管你的.


# # 多线程的第二种写法.  面向对象的写法
# class MyThread(Thread):  # 这玩意可以创建子线程
#
#     def __init__(self, name):  # self就是当前这个对象
#         # 这句话固定
#         super(MyThread, self).__init__()
#         # print("特意标记一下", name)
#         # print(self)
#         self.name = name
#
#
#     def run(self):  # run就是任务
#         print("我是run里面", self.name)
#         # for i in range(1000):
#         #     print('子线程', i)
#
#
# if __name__ == '__main__':
#     t1 = MyThread("alex")  # 直接创建出来了一个子线程
#     print(t1)
#     t1.start()  # 线程开始运行  ->  这里面会自动的让子线程去执行里面的run()这个功能
#
#     t2 = MyThread("wusir")  # 直接创建出来了一个子线程
#     t2.start()
#     # for j in range(999):
#     #     print("我是主线程", j)
