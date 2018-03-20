#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/16
import tracemalloc

ITEM_NUM = 10
class HaveSlots:
    __slots__ = ['item%s' % i for i in range(ITEM_NUM)]

    def __init__(self):
        for i in range(len(self.__slots__)):
            setattr(self, 'item%s' % i, i)

class NoSlots:
    def __init__(self):
        for i in range(ITEM_NUM):
            setattr(self, 'item%s' % i, i)


# 开始跟踪
tracemalloc.start()

obj = [NoSlots() for i in range(100)]
# 获取由 tracemalloc 模块跟踪的内存块的当前大小和峰值大小作为元组：(current: int, peak: int)
print(tracemalloc.get_traced_memory())

# 停止跟踪
tracemalloc.stop()

# 又开始跟踪，相当于重置
tracemalloc.start()
obj2 = [HaveSlots() for i in range(100)]
print(tracemalloc.get_traced_memory())

# (21832, 22219)    # 未定义__slots__字段，创建100个对象占用的内存约为 21832 字节
# (13760, 14147)    # 定义__slots__字段，创建100个对象占用的内存约为 13760 字节

