#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/7/29
"""
用multiprocessing 启用多进程。
"""
from multiprocessing import Process
import os
import time


def run(name):
    print("run child process %s[%s]" %(name, os.getpid()))
    time.sleep(1)

if __name__ == '__main__':
    print("Parent process %s" % os.getpid())
    for i in range(10):
        p = Process(target=run, args=(i,))
        print("process will start...")
        p.start()
        # p.join()  # join加上就是串行
