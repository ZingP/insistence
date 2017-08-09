#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/8/9

from collections import OrderedDict

dic = {
    "apple": 3,
    "pear": 7,
    "orange": 8,
    "banana": 10,
}

print(dic)
sort_dic2 = OrderedDict(sorted(dic.items()))
print(sort_dic2)

sort_dic = OrderedDict(dic)

print(sort_dic["apple"])
sort_dic["abc"] = 2  # 默认从最后插入

print(sort_dic)


