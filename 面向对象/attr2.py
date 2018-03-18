#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/18


class Salary(object):
    def __init__(self, money):
        # 基本工资
        self.basic_salary = money
        # 提成指数
        self.rate = 1.2

    def get_salary(self):
        return self.basic_salary * self.rate

    def set_salary(self, value):
        self.basic_salary = value

    def del_salary(self):
        del self.basic_salary

    salary = property(get_salary, set_salary, del_salary, "描述")

obj = Salary(20000.0)
print(obj.salary)

obj.salary = 30000.0
print(obj.salary)

del obj.salary
