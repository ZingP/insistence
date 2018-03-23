#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/22

class A:

    def __init__(self, name):
        self.name = name

    def hello(self):
        return "hello"

obj = A("liu")
setattr(obj, "age", 23)
print(obj.age)

r = getattr(obj, "hello")
print(r())

d = hasattr(obj, "hello")
print(d)
