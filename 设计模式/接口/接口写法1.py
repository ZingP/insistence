#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/5/11

# 接口：一种特殊的类，声明了若干抽象方法，要求继承该接口的类必须实现这些方法。可以理解为，接口就是一种抽象的基类，
# 限制继承它的类必须实现接口中定义的方法。
# 作用：限制继承接口的类的方法的名称及调用方式， 隐藏了类的内部实现。
# 下面Payment 这个类就是定义接口的
# 这种写法当不调用Alipay 中的pay方法时，是不报错的

class Payment(object):

    def pay(self, money):
        raise NotImplementedError


class ApplePay(Payment):

    def pay(self, money):
        print("Apple pay {} yuan.".format(money))


class AliPay(Payment):

    def fuqian(self, money):
        print("Ali pay {} yuan.".format(money))

a = AliPay()
# a.pay(200)

ApplePay().pay(300)


