#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/14


def sayHi(name: 'your name') -> 'say hi':
    print(f"Hi {name}")
    return

def func(x, y) -> ['hhh']:
    return x + y

sayHi("liuyouyuan")
a = func(1, 2)
print(a, type(a))
print(func.__annotations__)
print(sayHi.__annotations__)

# 在数值文字中使用下划线的能力
print('{:_}'.format(1000000))

