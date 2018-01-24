#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2018/1/23

import os
import time
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import gevent
from gevent import monkey
import threading
import requests

# import affinity
# cpu_count = os.cpu_count()
# print(cpu_count)
monkey.patch_all()

# def func(i):
#     url = "http://www.cnblogs.com/zingp/p/5878330.html"
#     res = requests.get(url=url)
#     print(i, res.status_code)


def func(i):
    print("协程：", i)
    gevent.sleep(1)
    print("线程id:", threading.current_thread())

def tell(i):
    print("进程", i, os.getpid())
    gevent_list = []
    for j in range(10):
        g = gevent.spawn(func, (j,))
        gevent_list.append(g)
    gevent.joinall(gevent_list)
    time.sleep(1)
    print(time.time())

if __name__ == '__main__':
    # 循环创建 10个子进程

    print(time.time())
    for i in range(10):
        # 创建子进程实例
        p = multiprocessing.Process(target=tell, args=(i,))
        # 运行子进程
        p.start()

    # ex = ProcessPoolExecutor(max_workers=8)
    # for i in range(1, 21):
    #     ex.submit(tell, (i,))
    # ex.shutdown(wait=True)   # 此函数用于释放异步执行操作后的系统资源。
    print("结束")