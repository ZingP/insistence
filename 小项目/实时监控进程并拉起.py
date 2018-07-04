#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/7/2

import os
import sys
import atexit
import subprocess
import time

def run_daemonize():
    pid = os.fork()
    if pid:
        sys.exit(0)
    os.chdir('/')
    os.umask(0)
    os.setsid()

    _pid = os.fork()
    if _pid:
        sys.exit(0)
    sys.stdout.flush()
    sys.stderr.flush()

    with open('/dev/null') as read_null, open('/dev/null', 'w') as write_null:
        os.dup2(read_null.fileno(), sys.stdin.fileno())
        os.dup2(write_null.fileno(), sys.stdout.fileno())
        os.dup2(write_null.fileno(), sys.stderr.fileno())
    atexit.register(os.remove)

def run_command(cmd):
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = p.communicate()[0]
    return output

def write_log(file_name, content):
    f = open(file_name, "a+")
    f.write(content)
    f.close()

if __name__ == '__main__':
    #run_daemonize()
    proc_dict = {
        "redis:6379": "restart-redis.sh",
        "redis:6389": "restart-safe-redis.sh",
        "redis:6399": "restart-safe-6399.sh",
    }
    log_file = "/search/odin/dt_op/scripts/check_proc_log.log"
    check_proc_cmd = "ps aux |grep {} |grep {} |grep -v grep"
    start_cmd = "'cd /search/odin/daemon/redis/ && sh {}'"
    while True:
        for k, v in proc_dict.items():
            proc, port = k.split(":")
            is_live_cmd = check_proc_cmd.format(proc, port)
            print(is_live_cmd)
            cmd_ret = run_command(is_live_cmd)
            restart_cmd = start_cmd.format(v)
            print("start cmd: {}".format(restart_cmd))
            if len(cmd_ret) == 0:
                print(123)
                report_time = time.strftime("%Y-%m-%d %X")
                try:
                    result = run_command(restart_cmd)
                except Exception as e:
                    result = e
                write_log(log_file, "{} {}\n".format(report_time, result))
        time.sleep(2)
