#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/8/3
"""
没有子节点的节点是叶节点，没有父节点的节点就是根节点。树的深度，就是有多少层
"""
import random
import time

def cost_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        cost = "cost_time>>:%s" % (end-start)
        return cost
    return wrapper


def sift(array, left, right):
    """调整"""
    i = left              # 当前调整的小堆的父节点
    j = 2*i + 1           # i的左孩子
    tmp = array[i]        # 当前调整的堆的根节点
    while j <= right:    # 如果孩子还在堆的边界内
        if j < right and array[j] < array[j+1]:     # 如果i有右孩子,且右孩子比左孩子大
            j = j + 1                               # 大孩子就是右孩子
        if tmp < array[j]:                          # 比较根节点和大孩子，如果根节点比大孩子小
            array[i] = array[j]                     # 大孩子上位
            i = j                                    # 新调整的小堆的父节点
            j = 2*i + 1                              # 新调整的小堆中I的左孩子
        else:                                       # 否则就是父节点比大孩子大，则终止循环
            break
    array[i] = tmp                                  # 最后i的位置由于是之前大孩子上位了，是空的，而这个位置是根节点的正确位置。


def heap(array):
    n = len(array)
    # 建堆，从最后一个有孩子的父亲开始，直到根节点
    for i in range(n//2 - 1, -1, -1):
        # 每次调整i到结尾
        sift(array, i, n-1)
    # 挨个出数
    for i in range(n-1, -1, -1):
        # 把根节点和调整的堆的最后一个元素交换
        array[0], array[i] = array[i], array[0]
        # 再调整，从0到i-1
        sift(array, 0, i-1)

array = list(range(100000))
random.shuffle(array)
heap(array)
print(array)

# 运行时间
import cProfile
cProfile.run('heap(array)')




