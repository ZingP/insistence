#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: "Zing-p"
# Date: 2017/8/19

import socket
import gevent

from gevent import monkey

monkey.patch_all()


def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)
    num = 0
    while True:
        print(num)
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)
        num += 1


def handle_request(conn):
    print("=====")
    try:
        while True:
            data = conn.recv(1024)
            print("recv:", data)
            conn.send(data.upper())
            if not data:
                conn.shutdown(socket.SHUT_WR)

    except Exception as ex:
        print(ex)
    finally:
        conn.close()


if __name__ == '__main__':
    server(9999)
