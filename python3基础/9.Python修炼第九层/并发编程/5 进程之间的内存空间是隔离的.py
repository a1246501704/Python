from multiprocessing import Process
import time,random

n=100
def task():
    global n
    n=0
    print('子',n)

if __name__ == '__main__':
    p=Process(target=task)
    p.start()  # 启动子进程时会将主进程的变量全部拷贝给子进程一份
    p.join()   
    print('主',n)
'''
子 0
主 100
'''