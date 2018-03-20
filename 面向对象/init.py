#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/20

# 构造方法，通过类创建对象时，自动触发执行。
class A:

    def __del__(self):
        pass

    def __init__(self, name):
        self.name = name
        print("this is __init__")

# 创建对象则自动触发__ini__方法。
obj = A("Jeo Chen")
# this is __init__