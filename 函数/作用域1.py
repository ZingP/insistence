#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/18

#1.第一种情况，外部函数a分别赋值给c.d两个变量，c又赋值给n,分别打印c、d、n的内存地址，得到三个变量都是指向同一个内存地址，
#是否可以说明最外层函数只能有一个内存地址?内层函数b被分别返回给x、y，可以看到x、y内存地址不同，彼此独立。但是x、y都引用
#了同一个全局变量n。
# n = 10
# def a():
#     print('外层函数被执行')
#     def b():
#         print('内层函数被执行，并且调用全局变量n：',n)
#         print(id(n))
#     return b
# c,d = a,a
# n = c
# print(c,d,n)
# x = a()
# y = a()
# print('内层函数返回给全局变量x内存地址:',x,'内层函数返回给全局变量y内存地址:',y)
# print('全局n:',n)
# x(),y()

a = 1
b = 1
print(id(a), id(b))

from copy import deepcopy
c = deepcopy(a)
d = deepcopy(a)
print(id(c), id(d))



