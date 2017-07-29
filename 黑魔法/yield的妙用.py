#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/7/29
"""
所有形如func()的函数，都可以改写成func1()以节约内存。
"""


def func():
    res = []
    for i in range(10):
        res.append(i)
    return res


def func1():
    for i in range(10):
        yield i

r = func()
print(r)
r1 = func1()
print(r1)

for j in r:
    print(j)
for k in r1:
    print(k)