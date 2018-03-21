#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/21

import threading
import time

def reduce_num(n):
    while n > 0:
        print("num::", n)
        time.sleep(5)
        n -= 1

t = threading.Thread(target=reduce_num, args=(10, ))
t.start()
t.join()
if t.is_alive():
    print("thread running.")
else:
    print("thread done.")




