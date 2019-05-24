#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

def genday_hours():
    li = []
    for i in range(24):
        if i < 10:
            li.append("0{}".format(i))
        else:
            li.append("{}".format(i))
    return li

cmd = "/usr/local/hadoop-client-mars/bin/hadoop fs -ls /storage/sogou/desktop/shouji/dt-shouji-java/201809/20180920|grep {}|grep 2018-09-20_{}|wc -l"


for item in genday_hours():
    cmds = cmd.format("and", item)
    print(cmds)
    os.system(cmds)