#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/23
class A:
    def __enter__(self):
        print("in __enter__")
        return [1, 2, 3]

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("in __exit__")

obj = A()
with obj as o:
    print("看看o是什么：", o)
    print("do something")
print("end")