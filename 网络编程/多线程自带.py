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
    time.sleep(2)

if __name__ == '__main__':
    ex = ThreadPoolExecutor(100)
    for i in range(1000):
        ex.submit(tell, (i,))
    ex.shutdown(wait=True)  # 此函数用于释放异步执行操作后的系统资源。

