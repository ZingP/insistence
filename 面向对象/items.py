#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/18

class Subject(object):

    # 静态字段
    subject = "数学科"

    def __init__(self, name):
        # 普通字段
        self.name = name

# 普通字段通过对象访问
obj = Subject("高等数学")    # 高等数学
print(obj.name)

# 静态字段通过类访问
print(Subject.subject)      # 数学科

# 通过对象去访问静态字段(不推荐)
print(obj.subject)          # 数学科

