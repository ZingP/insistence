#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/7/29
"""
子父进程、进程池中的进程之间的通信用Manager
"""

from multiprocessing import Pool, Manager
import os, time, random


def write(q):
    print('Process to write: %s' % os.getpid())
    for value in range(10):
        print('Put %s to queue...[write %s]' % (value, os.getpid()))
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    try:
        value = q.get(True,timeout=2)
        print('Get %s from queue.' % value)
    except Exception as e:
        print(e)


if __name__=='__main__':

    manager = Manager()
    q = manager.Queue()
    p = Pool(8)
    for i in range(20):
        p.apply_async(func=write, args=(q,),)
        p.apply_async(func=read, args=(q,))
    p.close()
    p.join()
    print("all done")
