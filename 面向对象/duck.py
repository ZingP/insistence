#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/17

class Dog(object):
    def talk(self):
        print("Wang wang!")

class Cat(object):
    def talk(self):
        print("Miao miao~~")

def animal_talk(obj):
    obj.talk()

# dog = Dog()
# cat = Cat()
# animal_talk(dog)
# animal_talk(cat)
# Wang wang!
# Miao miao~~

def talk(name, age, city):
    print("I am {}, {} years old, from {}".format(name, age, city))

talk("Liu yi fei", 30, "BJ")
talk("Liu you yuan", 25, "HB")
talk("Jeo Chen", 38, "TW")


class Person(object):
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def talk(self):
        print("I am {}, {} years old, from {}".format(self.name, self.age, self.city))

obj1 = Person("Liu yi fei", 30, "BJ")
obj1.talk()
obj2 = Person("Liu you yuan", 25, "HB")
obj2.talk()
obj3 = Person("Jeo Chen", 38, "TW")
obj3.talk()



