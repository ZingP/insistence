#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2018/1/23

import asyncio
import threading

@asyncio.coroutine
def func(i):
    print("协程", i, threading.currentThread())
    yield from asyncio.sleep(1)
    print("协程完", threading.currentThread())


# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(func(1))
# loop.close()

loop = asyncio.get_event_loop()
tasks = []
for i in range(20):
    g = func(i)
    tasks.append(g)
loop.run_until_complete(asyncio.wait(tasks))
loop.close()