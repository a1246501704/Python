#!/usr/bin/env python
#_*_coding:utf-8_*_

from conf import settings
import paramiko
import threading
import os

class Host_remote():
    '''
    批量远程管理用户组主机
    '''
    #初始化
    def __init__(self, host, port ,username, password, cmd):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.cmd = cmd

    def run(self):
        '''
        用进程 连接远程 主机后调用
        :return:
        '''
        cmd_str = self.cmd.split()[0]
        if hasattr(self, cmd_str):      #反射 :调用put方法
            getattr(self, cmd_str)()
        else:
            setattr(self, cmd_str, self.cmd)
            getattr(self, cmd_str)()  #调用cmd方法，执行批量命令处理

    def cmd(self):
        '''
        批量命令处理
        :return:
        '''
        ssh = paramiko.SSHClient()  #创建ssh对象
        #允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.host,port=self.port,username=self.username,password=self.password)
        stdin,stdout,stderr = ssh.exec_cmd(self.cmd)
        result = stdout.read()
        print("%s".center(40, "-") % self.host)
        print(result.decode())
        ssh.close()

    def put(self):
        '''
        发送文件
        :return:
        '''
        filename = self.cmd.split()[1]  #要上传的文件
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(filename, filename)
        print("put sucesss")

        transport.close()


def show_host_list():
    '''
    选择用户组 显示 主机名 与 IP
    :return:
    '''
    for index, key in enumerate(settings.host_dic):
        print("%s\033[34m 主机组:%s \033[0m \033[33m 主机数量:%s\033[0m" %(index + 1,key,len(settings.host_dic[key])))
    while True:
        choose_host_list = input(">>(请输入用户组编号如:group1): ").strip()
        host_dic = settings.host_dic.get(choose_host_list)
        if host_dic:
            for key in host_dic:
                print(key, host_dic[key]["IP"])
            return host_dic
        else:
            print("不退出此组!")


def interactive(choose_host_list):
    '''
    根据选择的 用户组的 主机起 多个线程进行 批量交互
    :param choose_host_list:
    :return:
    '''
    thread_list = []
    while True:
        cmd = input(">>: ").strip()
        if cmd:
            for key in choose_host_list:
                host, port, username, password = choose_host_list[key]["IP"], choose_host_list[key]["port"], \
                                                 choose_host_list[key]["username"], choose_host_listy[key]["password"]
                func = Host_remote(host, port, username, password, cmd)  # 实例化类
                t = threading.Thread(target=func.run)  # 起线程
                t.start()
                thread_list.append(t)
            for t in thread_list:
                t.join()  # 主线程等待子线程执行完毕
        else:
            continue


def run():
    choose_host_list = show_host_list()
    interactive(choose_host_list)

