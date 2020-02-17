#!/usr/bin/env python
#_*_coding:utf-8_*_

import getpass
from src.models import Admin


def initialize():
    try:
        user = input('请初始化用户名：')
        # pwd = getpass.getpass('请输入初始化密码：')
        pwd = input('请输入初始化密码：')
        obj = Admin(user,pwd)
        obj.save()
        return True
    except Exception as e:
        print(e)

def main():
    show = '''
        1.初始化管理员账号
    '''
    choice_dict = {
        '1':initialize
    }
    while True:
        print(show)
        choice = input('请输入操作选项：')
        if choice not in choice_dict:
            print('选项错误，请重新输入！！！')
        func = choice_dict[choice]
        ret = func()
        if ret:
            print('操作成功')
            return
        else:
            print('操作异常，请重新操作')
