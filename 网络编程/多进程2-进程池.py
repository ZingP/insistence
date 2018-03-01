#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/7/29

from multiprocessing import Pool
import time
import os


def run(name):
    print("run child process %s[%s]" % (name, os.getpid()))
    time.sleep(2)


def callback(name):
    print("callback %s.." % name)

if __name__ == '__main__':
    p = Pool(6)   # 我的机器四核，不写6默认是4
    for i in range(20):
        p.apply_async(func=run, args=(i,), callback=callback(i))
    p.close()
    p.join()
    print("all done...")

"""
对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close();
调用close()之后就不能继续添加新的Process了。不用join()父进程不会等待子进程直接结束。
"""
