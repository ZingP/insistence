#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: "Zing-p"
# Date: 2017/8/3
"""
单例就是只实例化一次。
"""


class Foo(object):
    __instance = None

    def __init__(self):
        self.name = "刘又源"

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            obj = object.__new__(cls, *args, **kwargs)
            cls.__instance = obj
        return cls.__instance


# 验证
obj1 = Foo()
obj2 = Foo()
print(id(obj1), id(obj2))
print(Foo)

"""
result:
59642736 59642736
<class '__main__.Foo'>
"""
