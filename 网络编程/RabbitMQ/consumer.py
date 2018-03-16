#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/15

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" 收到： %r" % body.decode("utf-8"))

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
print(' 等待。。。')
channel.start_consuming()

