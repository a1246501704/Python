#_*_coding:utf-8_*_


import os
import re

def init(func):
    def inner(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return inner

def search(filepath,target): #找到一个文件路径就往下个阶段传一次
    g = os.walk(filepath)
    for dirname, _, files in g:
        for file in files:
            abs_file_path = r'%s/%s' % (dirname, file)
            target.send(abs_file_path)

@init
def opener(target):
    while True:
        abs_file_path=yield
        with open(abs_file_path,'r') as f:
            target.send((f,abs_file_path))

@init
def cat(target):
    while True:
        f,abs_file_path=yield
        for line in f:
            res=target.send((line,abs_file_path))
            if res:
                break


@init
# def grep(pattern,target):
def grep(target):
    tag=False
    # pattern = pattern.encode('utf-8')
    while True:
        line,abs_file_path=yield tag
        tag=False
        # if pattern in line:
        abc = re.findall('[\u4e00-\u9fa5]',line)
        abc.encode('utf-8')
        # if re.findall('[\u4e00-\u9fa5]',line):
        if abc:
            target.send(abs_file_path)
            tag=True


@init
def printer():
    while True:
        abs_file_path=yield
        print(abs_file_path)


# search(r'/Users/zhuzhiwen/Downloads/py_s19/day7/',opener(cat(grep('你好',printer()))))
search(r'/Users/zhuzhiwen/Downloads/py_s19/day7/',opener(cat(grep(printer()))))

#
# with open(r'/Users/zhuzhiwen/Downloads/py_s19/day7/作业/test.py','r') as f:
#     for item in f:
#         # print(item)
#         # print(type(item))
#         print(re.findall('[\u4e00-\u9fa5]',item))
#
# print(re.findall('[\u4e00-\u9fa5]','a v 4 5 '))

#
# cat 1.txt | sed 's/[a-zA-Z0-9[:punct:]]//g' | grep -v '^$'
#
# Linux教程 - 正文 - 查找包含中文字符的文件
#
# 　　目的: 在一个目录下查找所有包含中文字符的文件
#
# 没有找到grep支持的正则表达式如何过滤中文字符, 虽然grep的man手册中标明-P参数可以支持perl语言的正则语法, 但使用下面命令会提示不支持这个参数:
#
#
# ~# grep -P "[\x80-\xff]" *
# grep: The -P option is not supported
# 　　偶然间找到一个叫pcregrep的工具, debian的描述是:
#
#
# pcregrep - grep utility that uses perl 5 compatible regexes.
# 　　安装后执行以下命令, 搞定:
#
# ~# pcregrep -r "[\x80-\xff]" *
#
# Excerpted from Linux教程 - 正文 - 查找包含中文字符的文件
# http://doc.linuxpk.com/54676.html
# Readability —  An Arc90 Laboratory Experiment  http://lab.arc90.com/experiments/readability
# Follow us on Twitter »Readability version 1.7.1





