#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/5
import heapq

# 从一个集合中获得最大或者最小的 N 个元素列表
# heapq 模块有两个函数：nlargest() 和 nsmallest() 可以完美解决这个问题
nums = [-5, -8, 9, 7, 10, 1, 2, 8, 5]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

heapq.heapify(nums)
print(nums)
print(nums[0])

print(heapq.heappop(nums))
print(heapq.heappop(nums))
print(heapq.heappop(nums))
print(heapq.heappop(nums))

print(max(nums))
print(min(nums))

# 注意列表是引用
# N=1 用max()或者min()
# 如果 N 的大小和集合大小接近的时候，通常先排序这个集合然后再使用切片操作会更快点。sorted(items)[:N]