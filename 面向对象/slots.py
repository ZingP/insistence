#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/16
import sys
# 创建大量对象时节省内存方法
class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

class FoolishDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

d = Date(2018, 3, 16)
d2 = FoolishDate(2018, 3, 16)

print(sys.getsizeof(d))
print(sys.getsizeof(d2))


