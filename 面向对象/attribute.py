#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/18

class Person(object):

    def __init__(self, name):
        self.name = name

    # 属性 与普通方法的区别就是加一个装饰器 @property
    @property
    def talk(self):
        return "my name is %s" % self.name

# 通过对象访问属性
# obj = Person("Liu You Yuan")
# print(obj.talk)     # my name is Liu You Yuan


class Salary(object):
    def __init__(self, money):
        # 基本工资
        self.basic_salary = money
        # 提成
        self.rate = 1.2

    @property
    def salary(self):
        return self.basic_salary * self.rate

    # 修改属性
    @salary.setter
    def salary(self, value):
        self.basic_salary = value

    # 删除属性
    @salary.deleter
    def salary(self):
        del self.basic_salary

# obj = Salary(20000)
# print(obj.salary)    # 24000.0  触发@property装饰的salary方法
#
# obj.salary = 30000
# print(obj.salary)    # 36000.0  触发@salary.setter装饰的salary方法
#
# del obj.salary       # 触发@salary.deleter装饰的salary方法

####################################################
class Person(object):

    def __init__(self, name):
        self.name = name

    def get_firstname(self):
        return self.name[:3]

    fistname = property(get_firstname)  # 自动返回get_firstname()的返回值

# obj = Person("Liu You Yuan")
# print(obj.fistname)      # Liu


