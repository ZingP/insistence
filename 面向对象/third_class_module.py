#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/19

class A:

    def func(self):
        pass

obj = A()
# 获取 [当前操作的对象] 所在的模块名
print(obj.__module__)
# __main__

# 获取 [当前操作的对象] 所在的类名
print(obj.__class__)
# <class '__main__.A'>


