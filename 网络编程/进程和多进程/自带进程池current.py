#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/1/26

import os
import time
import threading
from concurrent.futures import ProcessPoolExecutor

def func(i):
    print("进程", i, "进程ID", os.getpid(), "线程ID", threading.get_ident())
    time.sleep(2)


if __name__ == '__main__':
    pool = ProcessPoolExecutor(4)
    lis = []
    for i in range(10):
        lis.append(i)
        pool.submit(func, [i, ])
    pool.shutdown()
