#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/6

from collections import defaultdict
d = {}   # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

print(d)

pairs = {"a":1, "b":2, "c":[3, 4]}
d = {}
for key, value in pairs.items():
    if key not in d:
        d[key] = []
    d[key].append(value)
print(d)

# 如果使用 defaultdict 的话代码就更加简洁了：
d = defaultdict(list)
for key, value in pairs.items():
    d[key].append(value)
print(d)
