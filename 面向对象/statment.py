#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/16

# 定义一个 Dog 类
class Dog:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print("[{}]:Wang Wang Wang.".format(self.name))

# 创建对象
buck = Dog("buck")
# 调用对象中的talk()方法
buck.talk()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("Hello, my name is %s, i'm %s years old" % (self.name, self.age))

class Man(Person):
    def __init__(self, name, age):
        # 继承的第一种写法
        Person.__init__(self, name, age)

class Woman(Person):
    def __init__(self, name, age):
        # 继承的第二种写法
        super(Woman, self).__init__(name, age)

    def birth_children(self, p):
        print("[{}] birthed [{}]".format(self.name, p))


# # 封装到某处
# person1 = Person("YouYuan Liu", 25)
# person2 = Person("Jeo Chen", 38)
#
# # 访问属性
# print(person1.name)    # YouYuan Liu
# print(person2.name)    # Jeo Chen
#
# # 访问方法
# person1.hello()        # Hello, my name is YouYuan Liu, i'm 25 years old
# person2.hello()        # Hello, my name is Jeo Chen, i'm 38 years old

man1 = Man("YouYuan Liu", 25)
woman1 = Woman("Jeo Chen", 38)
print(man1.name)     # YouYuan Liu
man1.hello()         # Hello, my name is YouYuan Liu, i'm 25 years old
print(woman1.age)    # 38

woman1.birth_children("little Jeo")   # [Jeo Chen] birthed [little Jeo]
print(woman1.__class__)
print(woman1)