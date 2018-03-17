#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/17

class A:
    def run(self):
        print("run A")

class B(A):
    def run(self):
        super(B, self).run()
        print("run B")

class C(A):
    def run(self):
        super(C, self).run()
        print("run C")

class D(B, C):
    def run(self):
        super(D, self).run()
        print("run D")

class E(B, C):
    pass


a = A()
b = B()
c = C()
d = D()
e = E()

# b.run()  # A,B
# d.run()  # A,C,B,D
e.run()    # A, C, B





