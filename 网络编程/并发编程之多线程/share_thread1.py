#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/22
import time
from queue import Queue
from threading import Thread

# A thread that produces data
def producer(out_q, n):
    while n > 0:
        task = "任务%s" % n
        out_q.put(task)
        print("put>>", task)
        time.sleep(2)
        n -= 1

def consumer(in_q):
    while True:
        task = in_q.get()
        print("get>>", task)
        time.sleep(3)

# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q, 20,))
t1.start()
t2.start()
# Queue 对象已经包含了必要的锁，所以你可以通过它在多个线程间多安全地共享数据。 当使用队列时，协调生产者和消费者的关闭问题可能会有一些麻烦。
