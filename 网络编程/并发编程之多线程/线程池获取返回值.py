#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/27

import concurrent.futures
import requests

URLS = ['http://www.cnblogs.com/zingp/p/5878330.html',
        'http://www.cnblogs.com/zingp/',
        'https://docs.python.org/']

# 爬取网页内容
def load_url(url, timeout):
    with requests.get(url, timeout=timeout) as conn:
        return conn.text


with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 创建future对象和对应的url的字典
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as err:
            print('url:%s -- err: %s' % (url, err))
        else:
            print(url, len(data))

# http://www.cnblogs.com/zingp/ 12391
# http://www.cnblogs.com/zingp/p/5878330.html 90029
# https://docs.python.org/ 9980