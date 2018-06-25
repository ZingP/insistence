#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/25

# 用法
# lambada 参数,参数,参数 : 返回的表达式
# 示例1：
f = lambda x, y: x * y
print(f(2, 3))    # 6
# 示例2：
r = (lambda x, y: x+y)(1, 2)
print(r)          # 3

# filter(function, sequence)：对sequence中的item依次执行function(item)，
# 将执行结果为 True 的item组成一个filter对象（可迭代）（取决于sequence的类型）返回。
def gt_5(x):
    return x > 5

r = filter(gt_5, range(10))
print(list(r))      # [6, 7, 8, 9]


# map(function, sequence) ：对sequence中的item依次执行function(item)，见执行结果组成一个map对象（可迭代）返回
def mysum(x, y):
    return x + y

r = map(mysum, range(5), range(5, 10))
print(list(r))      # [5, 7, 9, 11, 13]

# reduce(function, sequence, starting_value)：对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值
# python3 中reduce已经冲全局名称空间里移除

from functools import reduce
r = reduce(mysum, range(10))
print(r)     # 45


def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)
r = reduce(lambda x, y: x + y, map(factorial, range(1, 11)))
print(r)    # 4037913