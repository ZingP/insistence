#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: "Zing-p"
# Date: 2017/8/3
"""
二分查找一定是基于有序序列。
"""
import random

def bin_search(data_set, val):
    low = 0                      # 第一个索引
    high = len(data_set) - 1     # 列表最后一个元素索引
    while low <= high:          # 当左边小于等于右边，只要列表还有元素
        mid = (low+high)//2      # 取列表中间的元素索引
        if data_set[mid] == val:  # 如果中间元素跟查找的相等，返回这个元素的索引？
            return mid
        elif data_set[mid] < val:   # 如果中间元素小于val,说明应该在右边找，那么low就等于mid+1
            low = mid + 1
        else:
            high = mid - 1          # 如果中间元素大于val，说明应该在左边找
    return

# ============== 应用 ==============
def random_list(n):
    """生成一大堆名字字典"""
    result = []
    ids = list(range(1001, 1001+n))
    a1 = ['赵', '钱', '孙', '李']
    a2 = ['力', '浩', '', '']
    a3 = ['强', '国']
    for i in range(n):
        dic = dict()
        dic['age'] = random.randint(18, 60)
        dic['id'] = ids[i]
        dic['name'] = random.choice(a1)+random.choice(a2)+random.choice(a3)
        result.append(dic)
    return result


def bin_use_search(data_set, val):
    """查找id为val的人。"""
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low+high)//2
        if data_set[mid]['id'] == val:
            return data_set[mid]
        elif data_set[mid]['id'] < val:
            low = mid + 1
        else:
            high = mid - 1
    return


if __name__ == '__main__':
    print(random_list(10))
    res = bin_use_search(random_list(123), 1050)
    print(res)


