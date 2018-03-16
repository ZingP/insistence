#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/16

# 如果想改变一个对象（示例）的显示效果，即当打印改对象时所能按需显示，可以重写类的__repr__和__str__方法。
class Point:
    """二维坐标系中的点"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        return "({0.x!s}, {0.y!s})".format(self)

point = Point(1, 2)
print(point)

# __repr__() 方法返回示例的字符串，当使用交互式解释器显示时会输出这个字符串。
# __str__() 方法将实例转换为一个字符串，使用 str() 或 print() 函数会输出这个字符串。
