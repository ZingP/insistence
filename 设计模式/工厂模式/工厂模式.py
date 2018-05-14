#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/5/14

from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):

    @abstractmethod
    def pay(self, money):
        pass

class ApplePay(Payment):
    def pay(self, money):
        print("苹果支付 {} 元.".format(money))

class AliPay(Payment):
    def __init__(self, enable_banlance=False):
        self.balance = enable_banlance

    def pay(self, money):
        if self.balance:
            print("余额宝支付 {} 元.".format(money))
        else:
            print("支付宝支付 {} 元.".format(money))

class PaymentFactory(object):
    def create_paymemt(self, method):
        if method == "alipay":
            return AliPay()
        elif method == "applepay":
            return ApplePay()
        elif method == "yuebao":
            return AliPay(enable_banlance=True)
        else:
            raise NameError(method)

# 使用
f = PaymentFactory()
p = f.create_paymemt("yuebao")
p.pay(3000)
# 余额宝支付 3000 元.



