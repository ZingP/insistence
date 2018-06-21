#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/21

# 给定N个整数的序列,计算连续子序列的最大和

def max_sub_sum(array):
    l = len(array)
    max_sum = 0
    for i in range(l):
        current_sum = 0
        for j in range(i, l):
            current_sum += array[j]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

def ma_sum_o_n(array):
    max_sum = current_sum = 0
    for i in range(0, len(array)):
        current_sum += array[i]
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
    return max_sum

if __name__ == '__main__':
    a = [3, -4, -1, 5]
    print(max_sub_sum(a))
    print(ma_sum_o_n(a))




