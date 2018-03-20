#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/19

class A:
    def __init__(self, string):
        self.string = string

    def __getslice__(self, i):
        print(i,j)
        return self.string[i:i+2]

    def __setslice__(self, i, j, sequence):
        self.string[i:j] = sequence

    def __delitem__(self, k):
        del self.string


obj = A("life is sort.")

print(obj[0:4])                 # 自动触发执行 __getslice__
obj[-2:3] = "using python."     # 自动触发执行 __setslice__
print(obj[:])

# del obj[0:2]                   # 自动触发执行 __delslice__
