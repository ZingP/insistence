#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/2/19


from pyquery import PyQuery as pq

url = "http://www.cnblogs.com/zingp/p/6863170.html"

res = pq(url)

print(res("#cnblogs_post_body").find('p'))