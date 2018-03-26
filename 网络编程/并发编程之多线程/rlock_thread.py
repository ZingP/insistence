#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/26

from threading import Thread
import time
import threading

rlock = threading.RLock()

def add_one(a):
    with rlock:
        a[1] += 1


def add_two(b):
    time.sleep(1)
    with rlock:
        b[1] += 2
        add_one(b)


if __name__ == '__main__':
    array = [0, 1, 4]
    thread_obj_list = []

    for i in range(50):
        t = Thread(target=add_two, args=(array,))
        t.start()
        thread_obj_list.append(t)

    for j in thread_obj_list:
        j.join()

    print("array result::", array)
    # array result:: [0, 151, 4]











