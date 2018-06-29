#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/26

# 动态导入模块
PLUGINS_DICT = {
    'cpu': 'src.plugins.cpu.CpuPlugin',
    'disk': 'src.plugins.disk.DiskPlugin',
    'main_board': 'src.plugins.main_board.MainBoardPlugin',
    'memory': 'src.plugins.memory.MemoryPlugin',
    'nic': 'src.plugins.nic.NicPlugin',
}

for k,v in PLUGINS_DICT.items():
    # module_path, cls_name = v.rsplit(".", 1)
    print(v.rsplit(".", 2))
    # print(module_path, cls_name)

