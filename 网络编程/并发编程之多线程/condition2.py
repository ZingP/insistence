#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/26

import threading
import time

condition = threading.Condition()    # 创建condition对象

def func(n):
    condition.acquire()    # 如果没有with语句，必写这句，否者报错
    condition.wait()       # 阻塞，等待其他线程调用notify()
    print("in func..", n)
    condition.release()    # 与acquire()成对出现

# 启10个线程
for i in range(10):
    t = threading.Thread(target=func, args=(i,))
    t.start()

time.sleep(5)

condition.acquire()
condition.notify(2)        # 通知两个线程执行
condition.release()

# in func..
# in func..
# 其他8个线程会继续等待。。。