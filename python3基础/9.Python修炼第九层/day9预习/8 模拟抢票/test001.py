#!/usr/bin/env python
#_*_coding:utf-8_*_

import json
import os
import time
from multiprocessing import Process,Lock

def search():
    dic=json.load(open('db.txt'))
    print('\033[32m[%s] 看到剩余票数<%s>\033[0m' %(os.getpid(),dic['count']))

def get_ticket():
    dic = json.load(open('db.txt'))
    time.sleep(0.5) #模拟读数据的网络延迟
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(0.5) #模拟写数据库的网络延迟
        json.dump(dic,open('db.txt','w'))
        print('\033[31m%s 购票成功\033[0m' %os.getpid())
    else:
        print('\033[31m%s 购票失败\033[0m' %os.getpid())

def task():
    search()
    mutex.acquire()
    get_ticket()
    mutex.release()

if __name__ == '__main__':
    mutex=Lock()
    for i in range(10):
        p=Process(target=task)
        p.start()



