#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/9/30

import json
import socket

host = 'localhost'
port = 9999
s = socket.socket()
s.connect((host, port))

f = open("111.jpg", "rb")
# msg = bytes(input(">>:"), encoding="utf8")
# chunk = f.read()
# s.sendall(chunk)
# file_size = len(f.read())
# data = {"filename": "111.jpg", "file_size": file_size, }
# while True:
# s.sendall(bytes(json.dumps(data), encoding="utf-8"))
result = s.recv(1024)
print(result)

if result == b"ok":
    s.sendfile(f)

    res2 = s.recv(1024)
    print(res2)
    s.close()
else:
    print("kkkkkkkkkkkkkk")

