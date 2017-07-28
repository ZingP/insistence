#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/7/23
"""
本模块用于测试闭包。
注意当for循环结束后，i一定是最后一次for循环的值。
补充一下闭包的概念，闭包概念比较复杂抽象，其中阮一峰谋篇博客有段个人理解我觉得可以借鉴：
    闭包就是能够读取其他函数内部变量的函数。由于在Python语言中，只有函数内部的子函数才能读取局部变量（global声明的除外），
因此可以把闭包简单理解成"定义在一个函数内部的函数。本质上，闭包就是将函数内部和函数外部连接起来的一座桥梁。
"""


def square():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = square()
print(f1(), f2(), f3())
print("闭包值：", f1.__closure__[0].cell_contents)


def square():
    fs = []
    for i in range(1, 4):
        def f(j=i):
             return j*j
        fs.append(f)
    return fs

f1, f2, f3 = square()
print(f1(), f2(), f3())
print("闭包值：", f1.__closure__)
"""
执行结果：
9 9 9
闭包值： 3
1 4 9
闭包值： None
前者是因为for循环结束后i始终为3；
后者是由于i每次都赋值给j,因而不存在闭包。
"""
