#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/9

def func():
    name = "liuyouyuan"

    def sayName():
        print(name)

    return sayName

f = func()
f()

"""
闭包是由函数和与其相关的引用环境组合而成的实体。
是引用了自由变量的函数，这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。
"""
