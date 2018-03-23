#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/22
import time
from threading import Thread

class A(Thread):
    def __init__(self,):
        super().__init__()

    def run(self):
        print("run1..", )
        time.sleep(5)
        print("run2..")

obj = A()
obj.start()
print("主线程结束")

if __name__ == '__main__':
    import multiprocessing
    obj = A()
    p = multiprocessing.Process(target=obj.run)
    p.start()
