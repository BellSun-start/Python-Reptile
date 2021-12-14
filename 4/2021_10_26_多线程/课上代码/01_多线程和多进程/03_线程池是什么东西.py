from concurrent.futures import ThreadPoolExecutor


def donwload(name):
    # 去下载图片
    print("我要下载图片")

    for i in range(1000):
        print(name, i)



# 100个任务. 能不能创建100个线程
# A, 能
# B, 不能
# 线程不是越多越好.
# 可以使用线程池来管理线程和任务之间的关系


if __name__ == '__main__':
    # 准备好10个任务, 2: 线程池中线程的个数
    with ThreadPoolExecutor(2) as t:  # 同时运行的任务只有2个 ?
        # 给线程池提交任务的第一种逻辑
        # for i in range(10):
        #     job = f"任务{i}" # 任务0, 任务1, 任务2, 任务3
        #     # Thread(target=xxx, args=(xxx))
        #     # 提交任务
        #     # 第一个参数: 任务
        #     # 后面的参数: 任务执行需要传递的信息
        #     t.submit(donwload, job) #

        #  给线程池提交任务的第二种逻辑
        # t.map(发钱, 155个人的名字)
        # t.map(donwload, ['任务0', '任务1', '任务2', '任务3', '任务4', '任务5', '任务6', '任务7', '任务8', '任务9'])
        pass

    print("我是主线程")

    # 自行总结: t.submit() 和t.map()的区别是什么???
