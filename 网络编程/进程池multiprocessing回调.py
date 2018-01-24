#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2018/1/24

import os
import time
from multiprocessing import Pool, Process

def run(i):
    print("start run...", i)
    time.sleep(1)
    return os.getpid(), i

def back(arg):
    print("arg", arg)
    time.sleep(1)
    print("callback", arg[0], arg[1], os.getpid())


if __name__ == '__main__':
    print(os.getpid())
    pool = Pool(4)
    for i in range(10):
        # 启动一个进程，执行run函数，run运行结束后返回值传给back函数
        pool.apply_async(func=run, args=(i, ), callback=back)
    pool.close()
    pool.join()  # 让主进程等待子进程执行完
