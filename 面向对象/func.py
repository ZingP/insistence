#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/18

class Person(object):

    def __init__(self, name):
        self.name = name

    # 普通方法 无装饰器  参数：self
    def talk(self):
        print("my name is %s" % self.name)

    # 类方法 装饰器:@classmethod 参数：cls(代表类本身)
    @classmethod
    def class_talk(cls):
        print("class Person")

    # 静态方法  装饰器:@staticmethod  参数：无
    @staticmethod
    def static_talk():
        print("static function")

# 通过对象调用普通方法
obj = Person("Jeo Chen")
obj.talk()               # my name is Jeo Chen

# 通过类调用类方法
Person.class_talk()      # class Person

# 通过类调用静态方法
Person.static_talk()     # static function







