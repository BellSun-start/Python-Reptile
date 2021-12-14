import asyncio
import time


async def func1():
    print('func1 - 入 1')
    # 发送网路请求
    # 休眠一下. 模拟网路请求
    await asyncio.sleep(2)  # 以前的sleep都是time.sleep(2)   2
    print('func1 - 出 2')


async def func2():
    print('func2 - 入 3')
    await asyncio.sleep(5)   # 5
    print('func2 - 出 4')


async def func3():
    print('func3 - 入 5')
    await asyncio.sleep(1)  # 1
    print('func3 - 出 6')


async def main():
    # 创建三个协程对象
    f1 = func1()
    f2 = func2()
    f3 = func3()

    # await 挂起, 让函数运行的时候. 允许被挂起.
    # 这样写是没法挂起的
    # await f1
    # await f2
    # await f3

    # 需要把三个任务封装在一个列表中. 统一进行挂起
    tasks = []
    # 创建三个任务
    t1 = asyncio.create_task(f1)
    t2 = asyncio.create_task(f2)
    t3 = asyncio.create_task(f3)

    tasks.append(t1)
    tasks.append(t2)
    tasks.append(t3)

    # 统一进行挂起, 等待三个任务全部完成. 才继续进行下去
    await asyncio.wait(tasks)
    print("呵呵哒")




    print("main结束")

if __name__ == '__main__':
    start = time.time()
    m = main()
    asyncio.run(m)
    end = time.time()
    print(end - start)
