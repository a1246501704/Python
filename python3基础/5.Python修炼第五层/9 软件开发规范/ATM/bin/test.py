#!/usr/bin/env python
#_*_coding:utf-8_*_

import os
import os.path
import re
import sys
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)

def read_json_conf(conf_path):
    if not os.path.exists(conf_path):
        return None
    sandbox_conf = {}
    #rb => r
    #py3,r 返回 str
    #py2,r 返回 str(bytes)
    with open(conf_path, 'r') as conf_f:
        sandbox_conf = json.loads(conf_f.read())
    return sandbox_conf

d = read_json_conf(base_dir+'/conf/service.cfg')
print(type(d))
print(d)

# print(base_dir)
# g = os.walk(base_dir)
# # print(g)
# # l = [i for i in g]
# # print(l)
# l1 = [('/Users/zhuzhiwen/Downloads/py_data/s19/day5/8 软件开发规范/ATM', ['bin', 'conf', 'core', 'db', 'lib', 'log'], []), ('/Users/zhuzhiwen/Downloads/py_data/s19/day5/8 软件开发规范/ATM/bin', [], ['start.py', 'test.py']), ('/Users/zhuzhiwen/Downloads/py_data/s19/day5/8 软件开发规范/ATM/conf', ['__pycache__'], ['service.cfg', 'settings.py']), ('/Users/zhuzhiwen/Downloads/py_data/s19/day5/8 软件开发规范/ATM/conf/__pycache__', [], ['settings.cpython-35.pyc']), ('/Users/zhuzhiwen/Downloads/py_data/s19/day5/8 软件开发规范/ATM/core', ['__pycache__'], ['src.py']), ('/Users/zhuzhiwen/Downloads/py_data/s19/day5/8 软件开发规范/ATM/core/__pycache__', [], ['src.cpython-35.pyc']), ('/Users/zhuzhiwen/Downloads/py_data/s19/day5/8 软件开发规范/ATM/db', [], []), ('/Users/zhuzhiwen/Downloads/py_data/s19/day5/8 软件开发规范/ATM/lib', ['aaa'], ['common.py']), ('/Users/zhuzhiwen/Downloads/py_data/s19/day5/8 软件开发规范/ATM/lib/aaa', [], ['__init__.py']), ('/Users/zhuzhiwen/Downloads/py_data/s19/day5/8 软件开发规范/ATM/log', [], [])]
# print('--------')
# for dirname, _, files in g:
#     print(files)
# #     print(dirname)