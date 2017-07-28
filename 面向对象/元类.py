#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/7/28


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
