#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/9/11

import functools

def login(func):
    """
    在这里从新定义一个高阶函数，
    这就是decorator。
    我们一会儿会仔细分析。
    """
    @functools.wraps(func)     # 这个装饰器是避免home函数的__name__属性改变
    def wrapper(*args, **kwargs):
        user = "zingp"   # 假设这是数据库中的用户名和密码
        passwd = "123"
        username = input("输入用户名：")
        password = input("输入密码：")
        if username == user and password == passwd:
            return func(*args, **kwargs)
        else:
            print("用户名或密码错误。")
    return wrapper


@login     # 利用python的@语法，把decorator置于home函数的定义处 相当于home = login(home)
def home():
    print("欢迎来到XX首页！")

home()
print(home.__name__)
