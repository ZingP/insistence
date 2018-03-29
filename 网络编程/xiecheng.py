
#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: "Zing-p"
# Date: 2017/8/19

from urllib import request
import gevent, time
from gevent import monkey

monkey.patch_all()    # 把当前程序中的所有io操作都做上标记

def spider(url):
    print("GET:%s" % url)
    resp = request.urlopen(url)
    data = resp.read()
    print("%s bytes received from %s.." % (len(data), url))

urls = [
    "https://www.python.org/",
    "https://www.yahoo.com/",
    "https://github.com/"
]

start_time = time.time()
for url in urls:
    spider(url)
print("同步耗时：", time.time() - start_time)

async_time_start = time.time()
gevent.joinall([
    gevent.spawn(spider, "https://www.python.org/"),
    gevent.spawn(spider, "https://www.yahoo.com/"),
    gevent.spawn(spider, "https://github.com/"),
])

print("异步耗时：", time.time() - async_time_start)

