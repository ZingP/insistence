#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/20

def __init__(self, name):
    self.name = name

def hello(self):
    print("hello {}".format(self.name))
# type()定义类， 第一个参数是类名，第二个参数是当前类的基类，第三个参数为类的成员
Person = type('Person', (object,), {'sayHi': hello, "__init__": __init__})

obj = Person("Liu")
print(obj)       # <__main__.Person object at 0x0000000002368E80>
obj.sayHi()      # hello Liu
