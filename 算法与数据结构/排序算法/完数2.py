#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/2/1

for i in range(2, 1001):
    k = []                # 列表k用于存储完数的所有因子
    n = -1
    s = i
    for j in range(1, i):
        if i % j == 0:
            n += 1        # n 是数组对应的指针
            s -= j
            k.append(j)
    if s == 0:
        print("完数：", i)
        print(" ".join([str(i) for i in k]))

