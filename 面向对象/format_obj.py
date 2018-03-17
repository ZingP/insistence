#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/16


# 通过 format() 函数和字符串方法使得一个对象能支持自定义的格式化
_formats = {
    'ymd-': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'ymd': '{d.year}{d.month}{d.day}'
    }

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd-'
        fmt = _formats[code]
        return fmt.format(d=self)


day = Date(2018, 3, 16)
print(format(day, "ymd"))
