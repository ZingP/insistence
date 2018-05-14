#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/5/14

# 创建一个单例基类，其他子类继承这个单例基类就是单例

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class MyName(Singleton):
    def __init__(self, name):
        self.name = name

a = MyName("Liuyouyuan")
print(a, a.name)
b = MyName("Jeo Chen")
print(b, b.name)

b.name = "CEO"
print(a.name)
# （1）注意a, b两个示例地址一样
# （2）修改了b.name, a.name 也会跟着改变