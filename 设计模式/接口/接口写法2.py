#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/5/11

# 抽象类加抽象方法就等于面向对象编程中的接口
# 这种写法，只要创建AliPay对象，就会报错
# 因为要求所有继承Payment的子类都必须要实习其定义的抽象方法

from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):

    @abstractmethod
    def pay(self, money):
        pass


class ApplePay(Payment):

    def pay(self, money):
        print("Apple pay {} yuan.".format(money))


class AliPay(Payment):

    def fuqian(self, money):
        print("Ali pay {} yuan.".format(money))

a = AliPay()

