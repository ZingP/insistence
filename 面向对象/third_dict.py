#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/19

class A:

    def __init__(self, name):
        self.name = name

    def func(self):
        pass


# 获取类的所有成员
print(A.__dict__)
#{'__module__': '__main__', 'func': <function A.func at 0x00000000025976A8>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}

# 获取对象的所有成员
obj = A("Liu You Yuan")
print(obj.__dict__)
# {'name': 'Liu You Yuan'}

list()
