#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/13

import socket

host = '10.143.57.161'
port = 9999
s = socket.socket()
s.connect((host, port))
data = "hello"
s.sendall(bytes(data, encoding="utf-8"))

result = s.recv(1024)
print(result)
