#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: "Zing-p"
# Date: 2017/8/3
"""
冒泡排序：
每趟相邻两数相比，大的往下沉；
一共进行n-1趟。
时间复杂度，o(n**2)
"""
import random
import cProfile

def bubble_sort(array):
    for i in range(len(array) - 1):
        status = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                status = True
        if not status:
            return

li = list(range(10000))
# li = list()
# for i in range(10000):
#     li.append(random.randint(0, 10000))
random.shuffle(li)
cProfile.run('bubble_sort(li)')
print(li)


