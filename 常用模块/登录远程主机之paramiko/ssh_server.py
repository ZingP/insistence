#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Liuyouyuan"
# Date: 2018/1/23

import paramiko

def run_cmd(host, port, user, passwd, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(cmd)

    stdout = stdout.read()
    stderr = stderr.read()
    ssh.close()
    if not stderr:
        print(stdout.decode())
    else:
        print(stderr.decode())

def run_cmd_pkey(host, port, user, rsa_file):
    """
    linux 端创建秘钥  ssh-keygen
    把要连的机子的公钥改名 mv id_rsa.pub authorized_keys
    想要连接哪台机器就直接把公钥copy到该机器的用户home下 格式：/root/.ssh
    """
    private_key = paramiko.RSAKey.from_private_key_file(rsa_file)  # 指定私钥所在文件
    ssh = paramiko.SSHClient()                                     # 创建ssh对象

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())               # 允许连接不在know_hosts文件中的主机
    ssh.connect(hostname=host, port=port, username=user, pkey=private_key)  # 连接服务器
    stdin, stdout, stderr = ssh.exec_command("df")                          # 执行命令

    stdout = stdout.read()
    stderr = stderr.read()
    ssh.close()                  # 关闭连接
    if not stderr:
        print(stdout.decode())
    else:
        print(stderr.decode())

def ssh_transfer_file(host, port, user, passwd, local_file, remote_file):
    transport = paramiko.Transport(host, port)
    transport.connect(username=user, password=passwd)
    sftp = paramiko.SFTPClient.from_transport(transport)
    # sftp.put(local_file, remote_file)            # 从本地上传文件到远程主机
    sftp.get(remote_file, local_file)              # 从远程主机下载到本地
    transport.close()


def ssh_transfer_file_pkey(host, port, user, rsa_file, local_file, remote_file):
    private_key = paramiko.RSAKey.from_private_key_file(rsa_file)   # 指定私钥所在文件
    transport = paramiko.Transport(host, port)
    transport.connect(username=user, pkey=private_key)
    sftp = paramiko.SFTPClient.from_transport(transport)

    sftp.put(local_file, remote_file)             # 从本地上传文件到远程主机
    # sftp.get(remote_file, local_file)           # 从远程主机下载到本地
    transport.close()

if __name__ == '__main__':
    HOST = "10.129.205.151"
    PORT = 22
    USER = "root"
    PASSWD = "admin123"
    cmd = "df -h"
    remote_file = "/data/download/nginx-1.12.0.tar.gz"
    local_file = "nginx-1.12.0.tar.gz"
    run_cmd(HOST, PORT, USER, PASSWD, cmd)
    # ssh_transfer_file(HOST, PORT, USER, PASSWD, local_file, remote_file)
