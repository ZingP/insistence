#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/13

import socket
import json

s = socket.socket()
s.bind(('127.0.0.1', 9999))
s.listen(500)
conn, addr = s.accept()

rec = conn.recv(1024)
print(rec)
