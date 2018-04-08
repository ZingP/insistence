#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/4/3
import socket
import time


host = 'localhost'
port = 9999
s = socket.socket()
s.connect((host, port))
# s = Socket(s)

# while True:
msg = input("请输入信息:")
s.sendall(bytes(msg, encoding='utf-8'))
time.sleep(2)


s.close()
