#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/8/3
import random
import cProfile

# 一次归并
def merge(array, low, mid, high):
    """
    两段需要归并的序列从左往右遍历，逐一比较，小的就放到
    tmp里去，再取，再比，再放。
    """
    tmp = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if array[i] <= array[j]:
            tmp.append(array[i])
            i += 1
        else:
            tmp.append(array[j])
            j += 1
    while i <= mid:
        tmp.append(array[i])
        i += 1
    while j <= high:
        tmp.append(array[j])
        j += 1
    array[low:high+1] = tmp


def merge_sort(array, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(array, low, mid)
        merge_sort(array, mid+1, high)
        merge(array, low, mid, high)

array = list(range(100000))
random.shuffle(array)
cProfile.run('merge_sort(array, 0, len(array)-1)')
print(array)










