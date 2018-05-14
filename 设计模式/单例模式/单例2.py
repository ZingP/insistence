#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/5/14

class A:
    var = 0

A.var = 1

a = A()
print(a.var)

# a.var = 1
b = A()
print(b.var)