#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/18

class Person(object):

    def __init__(self, name):
        self.name = name

    # 属性 与普通方法的区别就是加一个装饰器 @property
    @property
    def talk(self):
        return "my name is %s" % self.name

# 通过对象访问属性
obj = Person("Liu You Yuan")
print(obj.talk)     # my name is Liu You Yuan
