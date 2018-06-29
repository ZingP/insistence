#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/27

import socket

s = socket.socket()
s.bind(("127.0.0.1", 80))
s.listen()

while 1:
    print("start listening...")
    conn, addr = s.accept()
    print(conn, addr)
    requests = conn.recv(1024)
    print("requests:", requests)

    header = "HTTP/1.1 200 OK\r\n\r\n"  # http响应头
    data = "<h1>hello my web</h1>"      # 可以发html
    conn.send((header+data).encode("utf-8"))
    conn.close()
