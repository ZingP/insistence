#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/13

# Two simple generator functions
"""
(1) 在函数中，语句执行到yield，会返回yield 后面的内容；当再回来执行时，从yield的下一句开始执行。
(2) 使用yield语法的函数是一个生成器；
(3) python3中，通过 .__next__() 或者 next() 方法获取生成器的下一个值。
"""
from collections import deque

def sayHello(n):
    while n > 0:
        print("hello~", n)
        yield n
        n -= 1
    print('say hello')

def sayHi(n):
    x = 0
    while x < n:
        print('hi~', x)
        yield
        x += 1
    print("say hi")

# 使用yield语句，实现简单任务调度器
class TaskScheduler(object):
    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        '''
        向调度队列添加新的任务
        '''
        self._task_queue.append(task)

    def run(self):
        '''
        不断运行，直到队列中没有任务
        '''
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                # 生成器结束
                pass

# Example use
sched = TaskScheduler()
sched.new_task(sayHello(10))
sched.new_task(sayHello(5))
sched.new_task(sayHi(15))
sched.run()

# yield 就相当于挂起任务的信号

