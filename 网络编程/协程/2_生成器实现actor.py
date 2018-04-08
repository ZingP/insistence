#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/4/2
from collections import deque

class ActorScheduler:
    def __init__(self):
        self._actors = {}
        self._msg_queue = deque()

    def new_actor(self, name, actor):
        self._msg_queue.append((actor, None))
        self._actors[name] = actor

    def send(self, name, msg):
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor, msg))

    def run(self):
        while self._msg_queue:
            # print("队列：", self._msg_queue)
            actor, msg = self._msg_queue.popleft()
            # print("actor", actor)
            # print("msg", msg)
            try:
                 actor.send(msg)
            except StopIteration:
                 pass


if __name__ == '__main__':
    def say_hello():
        while True:
            msg = yield
            print("say hello", msg)

    def say_hi():
        while True:
            msg = yield
            print("say hi", msg)

    def counter(sched):
        while True:
            n = yield
            print("counter:", n)
            if n == 0:
                break
            sched.send('say_hello', n)
            sched.send('say_hi', n)
            sched.send('counter', n-1)

    sched = ActorScheduler()
    # 创建初始化 actors
    sched.new_actor('say_hello', say_hello())
    sched.new_actor('say_hi', say_hi())
    sched.new_actor('counter', counter(sched))

    sched.send('counter', 10)
    sched.run()

# ActorScheduler 负责事件循环
# counter() 负责控制终止
# say_hello() / say_hi() 相当于切换的协程，当程序运行到这些函数内部的yield处，就开始切换。