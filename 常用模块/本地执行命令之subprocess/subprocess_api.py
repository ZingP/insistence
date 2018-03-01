#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/1

import subprocess

def run_cmd(cmd):
    """
    这段代码执行一个指定的命令并将执行结果以一个字节字符串的形式返回。 如果你需要文本形式返回，加一个解码步骤即可。例如：
        out_text = out_bytes.decode('utf-8')
    如果被执行的命令以非零码返回，就会抛出异常。 
    默认情况下，check_output() 仅仅返回输入到标准输出的值。 如果需要同时收集标准输出和错误输出，使用 stderr 参数：
    """
    try:
        out_bytes = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        code = 0
    except subprocess.CalledProcessError as e:
        out_bytes = e.output
        code = e.returncode
    return [code, out_bytes.decode(encoding='utf-8')]

def run_cmd_popen(cmd):
    """执行命令,返回命令结果"""
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = p.communicate()[0]
    return output

def subprocess_run(cmd):
    """会直接打印出返回的结果"""
    subprocess.run(cmd, shell=True)




