#! /usr/bin/env python
# -*- coding: utf-8 -*-
\上述为文件头


\在python3中的input: 无论用输入何种类型，都会存成字符串类型。
name=input('please input your name: ') # name='zhangsan'  name='18'
print(name)
print (id(name),type(name),name)

\python2中input，用户必须输入带引号的值，输入的值是什么类型(例如输入：'egon'就存成str类型，输入:18就存成int类型)，就存成什么类型.开头添加 #!coding:utf-8 字符编码。
name=input('plese input your name: ')  # input时给个提示符，比如冒号、提示信息便于查看。
print(id(name),type(name),name)

\代码注释分单行和多行注释
    # 单行注释用#号
    # 多行注释可以用三对双引号""" """
# 代码注释的原则：
    # 1. 不用全部加注释，只需要在自己觉得重要或不好理解的部分加注释即可。
    # 2. 注释可以用中文或英文，但不要用拼音。
'''
多行注释

在python2中
raw_input与python3的input是一样的
name=raw_input('please input your name: ')
print(id(name),type(name),name)
'''

\练习
name=input('>>:请输入你的用户名: ')
password=input('>>:请输入您的密码: ')
print('您输入的用户名为:',name,'您输入的密码为:',password)
print(id(name),type(name),name)
print(id(password),type(password),password)
# >>:请输入你的用户名: zhanghongyang
# >>:请输入您的密码: 123
# 您输入的用户名为: zhanghongyang 您输入的密码为: 123
# 4353994096 <class 'str'> zhanghongyang
# 4353716776 <class 'str'> 123






