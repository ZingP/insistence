#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/7/23
"""
探究可迭代对象、迭代器、生成器之间的关系。
源码中Generator继承了Iterator，而Iterator继承了Iterable。
"""

from collections import Iterable
from collections import Iterator
from collections import Generator

print(isinstance([], Iterable))
print(isinstance([], Iterator))
print(isinstance([], Generator))

print(isinstance(iter([]), Iterable))
print(isinstance(iter([]), Iterator))
print(isinstance(iter([]), Generator))

print(isinstance((i for i in range(10)), Iterable))
print(isinstance((i for i in range(10)), Iterator))
print(isinstance((i for i in range(10)), Generator))

"""
知识总结：
容器：如列表、字典、元组、字符串、集合等数据类型；“通常，可以用来询问某个元素是否包含在其中时，那么这个对象就可以认为是一个容器”。

可迭代对象：凡是可以返回一个迭代器的对象都可称之为可迭代对象；迭代器内部持有一个状态，该状态用于记录当前迭代所在的位置，
以方便下次迭代的时候获取正确的元素。迭代器有一种具体的迭代器类型，比如list_iterator，set_iterator。
可迭代对象实现了__iter__方法，该方法返回一个迭代器对象。
    
迭代器：是一个带状态的对象，他能在你调用next()方法的时候返回容器中的下一个值，任何实现了__iter__和__next__()方法的对象都是迭代器，
__iter__返回迭代器自身，__next__返回容器中的下一个值，如果容器中没有更多元素了，则抛出StopIteration异常。

生成器：生成器算得上是Python语言中最吸引人的特性之一，生成器其实是一种特殊的迭代器，不过这种迭代器更加优雅。
它不需要再像上面的类一样写__iter__()和__next__()方法了，只需要一个yield关键字。
"""
