#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/1/24

import os
import time
import sys
from multiprocessing import Process

def run(name):
    print("第[{}]进程, 子进程ID：{}, 父进程ID：{}。".format(name, os.getpid(), os.getppid()))
    time.sleep(2)

if __name__ == '__main__':
    print("父进程ID：%s" % os.getpid())
    for i in range(10):
        p = Process(target=run, args=(i,))
        print("启动子进程...")
        if i == 5:
            sys.exit(0)
        p.start()
        # p.join()   # p.join加上就是串行,意思就是让主进程等待该子进程执行完成后再执行。
        # 不用p.join()进程就是并发的，主进程必然会等待子进程都结束才会退出。

