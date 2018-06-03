#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/7/28
"""
写代码是必须注意代码得运行效率，如果你无法判断那个高效，
可以采用cProfile分析函数的运行效率。或者自己写装饰器。
"""
import random
import cProfile
import time


def f1(li):
    l1 = sorted(li)
    l2 = [i for i in l1 if i<0.5]
    return [i*i for i in l2]


def f2(li):
    l1 = [i for i in li if i<0.5]
    l2 = sorted(l1)
    return [i*i for i in l2]


def f3(li):
    l1 = [i*i for i in li]
    l2 = sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]


def cost(func):
    """测试函数运行时间的装饰器。"""
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("执行时间：",  end_time-start_time)
    return deco


if __name__ == '__main__':

    li = [random.random() for i in range(100000)]
    cProfile.run('f1(li)')
    cProfile.run('f2(li)')
    cProfile.run('f3(li)')

"""
上述f1/f2/f3的运行效率是：f2 > f1 > f3.列表越小，排序效率越高。
"""

