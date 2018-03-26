#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/26
from threading import Thread
import time
import threading

lock = threading.Lock()

def add_one(a):
    time.sleep(1)
    # lock.acquire()
    with lock:
        a[1] += 1
    # lock.release()

if __name__ == '__main__':
    array = [0, 1, 4]
    thread_obj_list = []

    for i in range(50):
        t = Thread(target=add_one, args=(array,))
        t.start()
        thread_obj_list.append(t)

    for j in thread_obj_list:
        j.join()

    print("array result::", array)
    # array result:: [0, 51, 4]








