#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/1/26

import os
import time
from multiprocessing import Process

def run(*args, **kwargs):
    print("start run...", args)
    print(kwargs)
    print(__name__)
    time.sleep(1)
    return os.getpid(),

if __name__ == '__main__':
    p = Process(target=run, name="test", args=(1,), kwargs={"a": "b"})
    print("----", p.name)
    p.start()
