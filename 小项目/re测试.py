#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/29
import re

exp = "+/dddddd++//"
d = re.split('([\+\-\*\/\(\)])', exp)
# print(d)

# a = re.search('[\+\-\*\/\(]$', "2+(")
# a = re.search('^\-\d+\.*\d*$', "-3.000")
# print(a.group())
print('1.1'.isdigit())
