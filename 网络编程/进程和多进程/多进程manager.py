#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/2/12

from multiprocessing import Process, Manager
import time

def f1(d, q, i):
    d[str(i)] = i
    q.put(i)
    time.sleep(2)

def f2(d, q,):
    print("d::", d)

    print("q::", q.get())

if __name__ == '__main__':

    with Manager() as manager:
        d = manager.dict()
        q = manager.Queue()

        _objs = []
        for i in range(10):
            p = Process(target=f1, args=(d, q, i))
            _objs.append(p)
            p.start()

        for p in _objs:
            p.join()

        p = Process(target=f2, args=(d, q))
        p.start()
        p.join()
