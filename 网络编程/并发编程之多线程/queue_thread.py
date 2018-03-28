#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/27

from queue import Queue
import threading
import time

q = Queue(10)

def producer():
    n = 0
    while True:
        q.put("包子%s" % n)
        print("包子铺生产 包子%s" % n)
        n += 1
        time.sleep(2)

def consumer():
    while True:
        r = q.get()
        print("bucker 吃掉 %s" % r)
        time.sleep(1)

t1 = threading.Thread(target=producer)
t1.start()
t2 = threading.Thread(target=consumer)
t2.start()
