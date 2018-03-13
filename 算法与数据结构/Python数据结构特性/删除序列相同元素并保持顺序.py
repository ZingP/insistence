#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/13

""" 
序列中元素为 hashable 的时候,删除序列相同元素并保持顺序
"""
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = ["123", "4", "6", "9", "4", "7", "6"]
print(list(dedupe(a)))

"""
对于不可hash的，需要先转换成可hash对象
key参数指定了一个函数，将序列元素转换成 hashable 类型
"""
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))