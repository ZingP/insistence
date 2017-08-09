#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/8/9
"""
相当于一个进程池。
"""
from concurrent.futures import ProcessPoolExecutor
import time

def tell(i):
    print("this is process %s" % i)
    time.sleep(2)


if __name__ == '__main__':

    ex = ProcessPoolExecutor(max_workers=8)
    for i in range(1, 21):
        ex.submit(tell, (i,))
    ex.shutdown(wait=True)   # 此函数用于释放异步执行操作后的系统资源。
    print(123.0)



