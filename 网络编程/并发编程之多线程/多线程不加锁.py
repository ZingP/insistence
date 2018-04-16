#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/26

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/26
from threading import Thread
import time

def add_one(a):
    time.sleep(1)
    print("in thread a:", a)
    a[1] += 1

if __name__ == '__main__':
    array = [0, 1, 4]
    thread_obj_list = []

    for i in range(50000):
        t = Thread(target=add_one, args=(array,))
        t.start()
        thread_obj_list.append(t)

    for j in thread_obj_list:
        j.join()

    print("array result::", array)
    # array result:: [0, 51, 4]

# 有一个问题就是Python3中，为什么多线程在面对一些简单数据结构的时候，不加锁，也会得到正确的结果。难道是自动加锁了？









