#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: "Zing-p"
# Date: 2017/9/1


def der2(func):
    def wraper(*args, **kwargs):
        st = "oh "
        print("装饰器2中：", func)
        res = func()
        st += res
        print(st)
    return wraper


def deractor(func):
    def wraper(*args, **kwargs):
        st = "dear "
        print("装饰器1中:", func)
        res = func()
        st += res
        print(st)
        return st    # 必须返回
    return wraper

@der2
@deractor     # 先执行下面一个装饰器  顶层装饰器相当于装饰“包含第一个装饰器和原函数合并的”函数
def index():
    print("hello")
    return "hello"

index()

# 可以注意到两个装饰器中的func已经不一样了
"""
运行结果：
装饰器2中： <function deractor.<locals>.wraper at 0x0303D6F0>
装饰器1中: <function index at 0x0303D738>
hello
dear hello
oh dear hello
"""