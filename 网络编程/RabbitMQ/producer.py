#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/15

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))   # 相当于建立一个socket连接
channel = connection.channel()
# 声明queue
channel.queue_declare(queue='hello')
# RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='你好！'.encode("utf-8"))
print(" 发送 '你好！'")
connection.close()

