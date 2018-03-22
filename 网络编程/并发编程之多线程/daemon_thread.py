#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/22

# 对于需要长时间运行的线程或者需要一直运行的后台任务，你应当考虑使用后台线程。
import time
from threading import Thread

def func(n):
    while n > 0:
        with open('D:/githubfile/pythonclub/网络编程/并发编程之多线程/log.txt', 'a+') as f:
            print(str(n), file=f)
        n -= 1
        time.sleep(3)

t = Thread(target=func, args=(10,),daemon=True)
t.start()
t.join()
# time.sleep(90)