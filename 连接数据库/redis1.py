#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/27

import redis

r = redis.Redis(host='10.129.205.38', port=6379)
r.set('foo', 'Bar')
print(r.get('foo'))


