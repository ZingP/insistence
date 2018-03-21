#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/21
import time
from contextlib import contextmanager

class Person(object):

    def __init__(self, name):
        self.name = name
        self.list = []

    def __enter__(self):
        print("in __enter__")
        self.list.append(time.time())
        return self.list

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("in __exit__")
        self.list.pop()

# 来看一个装饰器版本的上下文管理器
# 检查代码消耗时间块
@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))

# 更高级的事务管理
@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working

lis = [1, 2, 3]
with list_transaction(lis) as work:
    work.append(5)
    work.append(6)

print(lis)
with list_transaction(lis) as work:
    work.append(5)
    work.append(6)
    # raise RuntimeError("oop")
print(lis)

with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1

with Person("Liu You yuan") as p:
    print(p[0])
    time.sleep(2)


