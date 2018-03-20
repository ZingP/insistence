#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/19

class A:
    def __init__(self, lis):
        self.lis = lis

    def __iter__(self):
        return iter(self.lis)

obj = A([2018, 0, 3, 1, 9])
for i in obj:    # 当对象用于迭代时，实际是相当于迭代__iter__方法的返回值。
    print(i)

# 2018
# 0
# 3
# 1
# 9

