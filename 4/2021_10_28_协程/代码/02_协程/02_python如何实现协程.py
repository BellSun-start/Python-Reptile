import asyncio  # 导包


async def func():
    print(123)


if __name__ == '__main__':
    f = func()  # sys:1: RuntimeWarning: coroutine 'func' was never awaited
    # 协程函数想要运行必须这样做
    # 1. 创建协程对象
    # print(f)

    # # 方案一
    # # 2. 想要运行协程对象必须要有一个超大号的event_loop -> 事件循环
    # event_loop = asyncio.get_event_loop()
    # # 3. 用event_loop运行协程对象. 让协程对象中的任务可以执行, 等待执行完毕
    # event_loop.run_until_complete(f)

    # # 方案二
    asyncio.run(f)   # 如果是windows的同学要注意. 这句话里面会有事件循环的关闭操作, 容易和windows的事件管理相冲突.
    # 如果你的电脑运行这句话出现了.  event_loop is closed ->  请更换为方案一即可
