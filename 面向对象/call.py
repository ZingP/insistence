#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/20

class A:
    def __call__(self):
        print("this __call__")

obj = A()
obj()   # 对象后面加括号，触发__call__
# this __call__
