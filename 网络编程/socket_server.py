#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/9/30

import socket
import json
s = socket.socket()
s.bind(('0.0.0.0', 9999))
s.listen(500)
# num = 0


conn, addr = s.accept()


rec = conn.recv(1024)
data = json.loads(rec)
print(data)
file_name = data.get("filename")
file_size = data.get("file_size")
print(file_name, file_size)
conn.sendall(b"ok")

size = 0
f = open("r.jpg", "a+")
while size < file_size:
    stream = conn.recv(8096)
    print(len(stream))
    f.write(str(stream))
    size += len(stream)
    print(size)
else:
    print("recv size:", size)
    conn.send(b"ok")
    f.close()
    conn.close()

