# 进程之间数据不共享,但是共享同一套文件系统,所以访问同一个文件,或同一个打印终端,是没有问题的,
# 而共享带来的是竞争，竞争带来的结果就是错乱，如何控制，就是加锁处理

\part1：多个进程共享同一打印终端
# 并发运行,效率高,但竞争同一打印终端,导致打印错乱
from multiprocessing import Process
import os,time

def work():
    print('%s print 1' %os.getpid())
    time.sleep(1)
    print('%s print 2' %os.getpid())
    time.sleep(1)
    print('%s print 3' % os.getpid())

if __name__ == '__main__':
    for i in range(3):
        p=Process(target=work)
        p.start()
'''
48295 print 1
48296 print 1
48297 print 1
48295 print 2
48296 print 2
48297 print 2
48295 print 3
48296 print 3
48297 print 3
'''


\不要用下面join的方式(join就把每个进程全部锁住了，第一个进程没有执行完，其他进程都无法执行。)
from multiprocessing import Process
import time,os,random

def task():
    print('%s print 1' %os.getpid())
    time.sleep(1)
    print('%s print 2' % os.getpid())
    time.sleep(1)
    print('%s print 3' % os.getpid())


if __name__ == '__main__':
    p1=Process(target=task)
    p2=Process(target=task)
    p3=Process(target=task)
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
'''
48340 print 1
48340 print 2
48340 print 3
48342 print 1
48342 print 2
48342 print 3
48343 print 1
48343 print 2
48343 print 3
'''


# 加锁：由并发变成了串行,牺牲了运行效率,但避免了竞争
from multiprocessing import Process,Lock
import os,time

def work(lock):
    lock.acquire()
    print('%s is running' %os.getpid())
    time.sleep(2)
    print('%s is done' %os.getpid())
    lock.release()
if __name__ == '__main__':
    lock=Lock()
    for i in range(3):
        p=Process(target=work,args=(lock,))
        p.start()
'''
48359 print 1
48359 print 2
48359 print 3
48360 print 1
48360 print 2
48360 print 3
48361 print 1
48361 print 2
48361 print 3
'''


# 这里只是一个引子，看3.1的案例
# 共享打印中断导致竞争，打印消息乱了。加上join牺牲了执行效率，保证了有序。原来的并发执行变成了串行执行。
# 这样用join实现没有意义，不用Process模块也可以实现。


