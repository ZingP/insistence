#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/21
import time
from contextlib import contextmanager

from socket import socket, AF_INET, SOCK_STREAM

class Connection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()


# conn = Connection(('www.python.org', 80))
# with conn as s1:
#     print(s1)
#     with conn as s2:
#         print(s2)

import time
from contextlib import contextmanager
# 来看一个装饰器版本的上下文管理器
# 检查代码消耗时间块
@contextmanager
def timecount(name):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(name, end - start))

# with timecount('cost time:'):
#     time.sleep(2)
# cost time:: 2.000200033187866

# 更高级的事务管理
@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working

lis = [1, 2, 3]
with list_transaction(lis) as work:
    work.append(5)
    work.append(6)
    print(lis)
    raise RuntimeError("回滚")
# print(lis)

# with list_transaction(lis) as work:
#     work.append(5)
#     work.append(6)
#     raise RuntimeError("oop")
# print(lis)




