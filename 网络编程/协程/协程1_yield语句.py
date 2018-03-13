#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/13

# Two simple generator functions
"""
(1) 在函数中，语句执行到yield，会返回yield 后面的内容；当再回来执行时，从yield的下一句开始执行。
(2) 使用yield语法的函数是一个生成器；
(3) python3中，通过 .__next__() 或者 next() 方法获取生成器的下一个值。
"""
def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield n
        n -= 1
    print('Blastoff!')

def countup(n):
    x = 0
    while x < n:
        print('Counting up', x)
        yield
        x += 1
x = countdown(10)
print(x.__next__())
print(next(x))
x.__next__()
# x.__next__()


