#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/1/26

import os
import time
import threading
from concurrent.futures import ProcessPoolExecutor

my_list = []
def func(i):
    print("进程", i, "进程ID", os.getpid(), "线程ID", threading.get_ident())
    time.sleep(1)


if __name__ == '__main__':
    pool = ProcessPoolExecutor(4)
    pool.map(func, list(range(10)))
    pool.shutdown()
    print(my_list)    # 进程间不能这么通讯
