#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/20

class A:

    def __init__(self, name):
        print("In A init")
        self.name = name

    def __new__(cls, *args, **kwargs):
        print("In A new",)
        return object.__new__(cls)

# 创对象
# obj = A("Liu You Yuan")
# In A new
# In A init

class Person:

    def __init__(self, name):
        print("in Person init")
        self.name = name

    def __new__(cls, *args, **kwargs):
        print("In Person new",)
        return object.__new__(cls)

# 不调用 __init__() 方法来创建Person对象
obj = Person.__new__(Person)
print(obj)
print(obj.name)

