#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/4/16

import subprocess
from concurrent.futures import ThreadPoolExecutor

class SshExc(object):

    def __init__(self, hosts, cmds, max_worker=50):
        self.hosts = [h for h in hosts]
        self.cmds = [c for c in cmds]
        self.max_worker = max_worker   # 最大并发线程数
        self.success_hosts = []
        self.failed_hosts = []   # 存放失败的机器IP

    @staticmethod
    def run_cmd(cmd):
        """本地执行命令。"""
        try:
            out_bytes = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            code = 0
        except subprocess.CalledProcessError as e:
            out_bytes = e.output
            code = e.returncode
        return [code, out_bytes.decode(encoding='utf-8')]

    @staticmethod
    def color_str(old, color=None):
        if color == "red":
            new = "\033[31;1m{}\033[0m".format(old)
        elif color == "yellow":
            new = "\033[33;1m{}\033[0m".format(old)
        elif color == "blue":
            new = "\033[34;1m{}\033[0m".format(old)
        elif color == "green":
            new = "\033[36;1m{}\033[0m".format(old)
        else:
            new = old
        return new

    def gene_remote_cmd(self, host):
        st = "ssh {} '{}'"
        return [st.format(host, c) for c in self.cmds]

    def execute(self, host):
        """单台机器上串行执行命令，并返回结果至字典"""
        result = list()
        final_cmds = self.gene_remote_cmd(host)
        for c in final_cmds:
            r = self.run_cmd(c)
            result.append([c, r])
        return host, result

    def run(self):
        """并发执行"""
        future = ThreadPoolExecutor(self.max_worker)
        for h in self.hosts:
            try:
                future.submit(self.execute, h).add_done_callback(self.callback)
            except Exception as err:
                err = self.color_str(err, "red")
                print(err)
        future.shutdown(wait=True)

    def callback(self, obj):
        """回调函数，处理返回结果"""
        host, rlist = obj.result()
        print(self.color_str("{} execute detail:".format(host), "yellow"))
        is_success = True   # 对于一台机器，命令是否全部执行成功
        for item in rlist:
            cmd, [code, res] = item
            info = f"{cmd} | code => {code}\nResult:\n{res}"
            if code != 0:
                info = self.color_str(info, "red")
                is_success = False
                if host not in self.failed_hosts:
                    self.failed_hosts.append(host)
            else:
                # 执行成功
                info = self.color_str(info, "green")
            print(info)
        if is_success:
            self.success_hosts.append(host)
            if host in self.failed_hosts:
                self.failed_hosts.remove(host)

    def handle_fail_hosts(self):
        """由于并发某些命令, 可能会失败，对失败机器从新执行"""
        while len(self.failed_hosts) != 0:
            self.hosts = self.failed_hosts
            self.run()

    def overview(self):
        """展示中的执行结果"""
        for i in self.success_hosts:
            print(self.color_str(i, "green"))
        print("-" * 30)
        for j in self.failed_hosts:
            print(self.color_str(j, "red"))
        info = "Success hosts {}; Failed hosts {}."
        s, f = len(self.success_hosts), len(self.failed_hosts)
        info = self.color_str(info.format(s, f), "yellow")
        print(info)

if __name__ == '__main__':

    hosts = []
    cmds = []
    obj = SshExc(hosts, cmds)
    obj.run()
    obj.overview()