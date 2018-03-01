#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/1

import logging

def logger_set():
    """
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0
    """
    logging.basicConfig(
        filename='mylog.log',
        format='%(asctime)s %(levelname)s %(module)s [%(message)s]',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r ", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')

if __name__ == '__main__':
    logger_set()


