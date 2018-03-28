#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/27

import time
import threading

def func(n):
    while n > 0:
        print("线程name:", threading.current_thread().name, "参数n:", n)
        n -= 1
        time.sleep(1)

t = threading.Thread(target=func, args=(2,))
t.start()
t.join()
print("主线程：", threading.current_thread().name)
print("主线程结束")
# 运行结果：
# 线程name: Thread-1 参数n: 2
# 线程name: Thread-1 参数n: 1
# 主线程： MainThread
# 主线程结束


