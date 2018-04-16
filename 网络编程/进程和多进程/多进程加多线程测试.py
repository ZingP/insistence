#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/4/16

from multiprocessing import Process
import threading
import time

lis = [0, 1, 2]

def addOne(li):
    num = 100
    while num > 0:
        time.sleep(0.5)
        li[0] += 1
        num -= 1
    print(threading.currentThread().ident, li[0])


def func(li):
    _obj = []
    for i in range(10):
        t = threading.Thread(target=addOne, args=(li,))
        _obj.append(t)

    for i in range(5):
        t = threading.Thread(target=addOne, args=(li,))
        _obj.append(t)

    for o in _obj:
        o.start()

if __name__ == '__main__':
    p = Process(target=func, args=(lis,))
    p.start()
    p.join()
    print(lis)

