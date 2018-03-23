#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/22

# 对于需要长时间运行的线程或者需要一直运行的后台任务，你应当考虑使用后台线程。
import time
import threading

def func(n):
    while n > 0:
        print("参数n:", n)
        n -= 1
        time.sleep(1)

t = threading.Thread(target=func, args=(10, ), daemon=True)
t.start()
time.sleep(3)
print("主线程结束")

# 参数n: 10
# 参数n: 9
# 参数n: 8
# 参数n: 7
# 主线程结束