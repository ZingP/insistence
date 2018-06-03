#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/5/31

import uuid
import time
import tracemalloc
import gc
import sys


class Class(object):
    def __init__(self, classid):
        self.classid = classid
        self.whatever = self.nothing

    def nothing(self):
        print('123')


if __name__ == '__main__':

    tracemalloc.start()
    li = []
    for i in range(500000):
        li.append(Class(uuid.uuid1()))
    print(li[1].classid)
    print(sys.getrefcount(li))   # 查看引用计数
    print('create instance')
    print(tracemalloc.get_traced_memory())
    # tracemalloc.stop()
    # time.sleep(10)
    li.clear()
    # del li[:]
    li = ""
    # tracemalloc.start()
    print('release instance')
    print(tracemalloc.get_traced_memory())
    gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
    gc.set_debug(gc.DEBUG_COLLECTABLE)

    while True:
        # print(gc.get_threshold())    # 查看阈值
        time.sleep(10)
        print(tracemalloc.get_traced_memory())
        # gc.collect()
    # Python不停地更新着众多引用数值。特别是当你不再使用一个大数据结构的时候，比如一个包含很多元素的列表，Python可能必须一次性释放大量对象。
    # 减少引用数就成了一项复杂的递归过程了。