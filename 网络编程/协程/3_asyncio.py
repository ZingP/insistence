#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/4/3

import asyncio

@asyncio.coroutine
def say_hi(n):
    print("start:", n)
    r = yield from asyncio.sleep(2)
    print("end:", n)

# loop = asyncio.get_event_loop()
# tasks = [say_hi(0), say_hi(1)]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# start: 1
# start: 0
# 停顿两秒
# end: 1
# end: 0
async def say_hi(n):
    print("start:", n)
    r = await asyncio.sleep(2)
    print("end:", n)

loop = asyncio.get_event_loop()
tasks = [say_hi(0), say_hi(1)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# start: 1
# start: 0
# 停顿两秒
# end: 1
# end: 0
