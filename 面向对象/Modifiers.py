#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/18

class Person:

    Country = "China"
    __P = "SC"

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __hello(self):
        print("[{}] age is [{}]".format(self.name, self.__age))

    def hi(self):
        self.__hello()

obj = Person("Liu You Yuan", 23)
print(obj.name)      # 访问公有成员

# print(Person.__P)  # 报错，外部不能访问
# print(obj.__age)   # 报错，外部不能访问

# 强制访问可以
print(obj._Person__age)    # 23

obj.hi()    # [Liu You Yuan] age is [23]
