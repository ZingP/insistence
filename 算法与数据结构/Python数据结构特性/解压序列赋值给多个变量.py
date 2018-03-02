#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/2

# 解压赋值可以用在任何可迭代对象上面
person_info = ["liuyy", "male", "18566666", "010-62332345"]
name, sex, *phone = person_info
print(name, sex, phone)

record = ('LIUYY', 65, 175, (3, 2, 2018))
name, *_, (*_, year) = record
print(name, year, _)