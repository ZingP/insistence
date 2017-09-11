#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/8/12

import os
import sys
import platform

# dirname 获取路径的目录；__file__获取当前文件的绝对路径
if platform.system() == 'Windows':
    BASE_DIR = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
else:
    BASE_DIR = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(BASE_DIR)

print(__file__)    # 路径以 / 分割
print(os.path.abspath(__file__))   # 路径以 \ 分割