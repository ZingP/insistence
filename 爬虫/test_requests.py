#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/21

import requests
import time

url = "http://www.cnblogs.com/zingp/"
response = requests.get(url)
print(response.status_code)
time.sleep(5)
print(response.text)


