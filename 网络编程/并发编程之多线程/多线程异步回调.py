#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/28

from concurrent.futures import ThreadPoolExecutor
import time
import threading

def tell(i):
    print("this is tread {}.".format(i))
    time.sleep(1)
    return [i, threading.get_ident()]   # 必须有返回

def callback(obj):           # 必须有参数
    result = obj.result()
    print(result)

if __name__ == '__main__':
    future = ThreadPoolExecutor(10)
    a = "ddd"
    for i in range(100):
        # 会将线程future对象传给callback
        future.submit(tell, i,).add_done_callback(callback)   # 添加一个线程到线程池
    future.shutdown(wait=True)      # 此函数用于释放异步执行操作后的系统资源。
