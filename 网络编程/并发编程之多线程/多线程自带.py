#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/8/9
"""
自带线程池。
"""

from concurrent.futures import ThreadPoolExecutor
import time

def tell(i):
    print("this is tread {}.".format(i))
    time.sleep(3)
    return i

if __name__ == '__main__':
    future = ThreadPoolExecutor(10)
    a = "ddd"
    for i in range(100):
        r = future.submit(tell, (i,)).result()   # 添加一个线程到线程池

    future.shutdown(wait=True)      # 此函数用于释放异步执行操作后的系统资源。


