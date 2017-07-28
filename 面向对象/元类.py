#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/7/28
"""
该模块的主要探究类是type类实例化创建，以及类的实例化过程。
"""


class MyType(type):

    def __init__(self, child_cls, bases=None, dict=None):
        print("In MyType init")
        super(MyType, self).__init__(child_cls, bases, dict)

    def __new__(cls, *args, **kwargs):
        print("In MyTyPe new")
        return type.__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("In MyType call:")
        obj = self.__new__(self, args, kwargs)
        self.__init__(obj, *args, **kwargs)


class Foo(object, metaclass=MyType):

    def __init__(self, name):
        print("In Foo init")
        self.name = name

    def __new__(cls, *args, **kwargs):
        print("In Foo new",)
        return object.__new__(cls)

obj = Foo("zing-p")

"""
运行代码得结果：
In MyTyPe new
In MyType init
In MyType call:
In Foo new
In Foo init

知识点：
第一阶段：解释器从上到下执行代码创建Foo类(也就是说Foo是元类的一个实例),new触发init实例化类。
第二阶段：通过Foo类创建obj对象。类名加括号触发call,call再调new~~~
注意：类中有一个属性 metaclass，其用来表示该类由“谁”来实例化创建，所以，我们可以为 metaclass 设置一个type类的派生类，从而查看类创建的过程。
"""