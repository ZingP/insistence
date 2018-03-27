#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/27

import time
import threading

bar = threading.Barrier(3)  # 创建barrier对象，指定满足3个线程

def worker1():
    print("worker1")
    time.sleep(1)
    bar.wait()
    print("worker1 end")

def worker2():
    print("worker2")
    time.sleep(2)
    bar.wait()
    print("worker2 end")

def worker3():
    print("worker3")
    time.sleep(5)
    bar.wait()
    print("worker3 end")


thread_list = []
t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)
t3 = threading.Thread(target=worker3)
thread_list.append(t1)
thread_list.append(t2)
thread_list.append(t3)

for t in thread_list:
    t.start()

# 每个线程中都调用了wait()方法，在所有（此处设置为3）线程调用wait方法之前是阻塞的。
# 也就是说，只有等到3个线程都执行到了wait方法这句时，所有线程才继续执行。
