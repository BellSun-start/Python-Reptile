import asyncio

async def func1():
    print("我是func1-入")
    await asyncio.sleep(1)
    print("我是func1-出")
    return "我爱你-1"

async def func2():
    print("我是func2-入")
    await asyncio.sleep(1)
    print("我是func2-出")
    return "我爱你-2"

async def func3():
    print("我是func3-入")
    await asyncio.sleep(99999)
    print("我是func3-出")
    return "我爱你-3"

async def main():
    f1 = func1()
    f2 = func2()
    f3 = func3()

    tasks = []
    # 在创建任务的时候. 已经就开始执行了
    tasks.append(asyncio.create_task(f1))  # 1, 2, 3
    tasks.append(asyncio.create_task(f2))  # 2, 1, 3
    tasks.append(asyncio.create_task(f3))  # 3, 1, 2
    # # 所有的任务一起统一的进行等待
    # 第一套返回值
    # a, b = await asyncio.wait(tasks)
    # for item in a:  # 循环a这个集合, 如果你的python是3.8以上
    #     print(item.result())  # 拿到返回值

    # # 第二套返回值, 直接获取到返回值
    # result = await asyncio.gather(*tasks)  # python基础. 动态传参
    # print(result)  # gather收集返回值的时候. 是按照你给的任务的顺序来收集. 所以它是有序的.


if __name__ == '__main__':
    asyncio.run(main())
