#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/4/1
name = "lyy"
age = "26"
print(f"I am {name}, {age} years old.")

dic = {'name': "lyy", 'age': 26}
string = "{name}-{age}".format(**dic)
print(string)

li = ["liuyouyuan", 26]
print("{}-{}".format(*li))

