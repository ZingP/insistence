#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2018/1/5


import gevent
from gevent import monkey

monkey.patch_all()


def func(i):
    print(i)
    gevent.sleep(2)

gevent_li = []
for i in range(10):
    g = gevent.spawn(func, i)
    g.join()

print("完了")
