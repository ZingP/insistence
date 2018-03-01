#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/2/1

from sys import stdout

for i in range(2, 1001):
    k = []                # 列表k用于存储完数的所有因子
    n = -1
    s = i
    for j in range(1, i):
        if i % j == 0:
            n += 1  # n是数组对应的指针
            s -= j
            k.append(j)

    if s == 0:
        print("完数：", i)
        for j in range(n):  # 此处的j和上面代码中的j不一样，是独立的。目的在于遍历列表K中的元素不包括最后一个元素，并打印。
            stdout.write(str(k[j]))  # 在标准输出中打印列表k中下标为j的元素
            stdout.write(' ')        # 在标准输出打印空字符串
        print(k[n])                  # 打印列表k的最后一个元素

# 在Python中[]叫列表，不是数组，功能和C语言中的额数组类似。