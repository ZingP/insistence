#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/7/4
import random

def select_2(array, val):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low+high) // 2
        if array[mid] == val:
            return mid
        elif array[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return

def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


a = list(range(2, 1000))
random.shuffle(a)
print(a)
bubble_sort(a)
print(a)



