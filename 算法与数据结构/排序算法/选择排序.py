#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/7/5

import random
def select_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

array = list(range(100))
random.shuffle(array)
print(array)
select_sort(array)
print(array)