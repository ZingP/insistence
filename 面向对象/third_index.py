#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/19
# __getitem__ / __setitem__ / __delitem__
class Person:

    def __init__(self, name):
        self.name = name

    def __getitem__(self, k):
        return self.name

    def __setitem__(self, k, v):
        self.name = v

    def __delitem__(self, k):
        del self.name


obj = Person("Jeo Chen")

result = obj['name']          # 自动触发执行 __getitem__
print(result)                 # Jeo Chen

obj['name'] = 'Liu You Yuan'  # 自动触发执行 __setitem__
print(obj['name'])            # Liu You Yuan

print(obj[1:2])

del obj['name']               # 自动触发执行 __delitem__

