#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/21
import time
import sys
# 给定N个整数的序列,计算连续子序列的最大和
sys.setrecursionlimit(10000)

def cost_time(func):
    def wapper(*args, **kwargs):
        start = time.time()
        m_sum = func(*args, **kwargs)
        end = time.time()
        print("Cost time:{}".format(end - start))
        return m_sum
    return wapper

# O(n^2)复杂度
@cost_time
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

# O(n)复杂度
@cost_time
def ma_sum_o_n(array):
    max_sum = current_sum = 0
    for i in range(0, len(array)):
        current_sum += array[i]
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
    return max_sum

def max_sum_nln(array):
    left = 0
    right = len(array)
    print(left, right)

    if right-left == 1 or left == right:
        print(array[left])
        if array[left] > 0:
            return array[left]
        else:
            return 0

    center = (left + right) // 2  # 中分点
    print("center", center)

    max_left_sum = max_sum_nln(array[left:center])
    max_right_sum = max_sum_nln(array[center: right])

    left_sum = left_max_sum = 0
    i = center
    while i >= left:
        left_sum += array[i]
        if left_sum > left_max_sum:
            left_max_sum = left_sum
        i -= 1

    right_sum = right_max_sum = 0
    j = center+1
    while j < right:
        right_sum += array[i]
        if right_sum > right_max_sum:
            right_max_sum = right_sum
        j += 1

    return max([max_left_sum, max_right_sum, left_max_sum+right_max_sum])


if __name__ == '__main__':
    import random
    list_a = list(range(-100, 100))
    random.shuffle(list_a)
    print(list_a)
    print(ma_sum_o_n(list_a))
    print(max_sub_sum(list_a))
    # print(max_sum_nln(list_a))


