#文件db的内容为：{"count":1}
#注意一定要用双引号，不然json无法识别

from multiprocessing import Process,Lock
import json
import time
import random
import os

# 查票数
def search():
    data=json.load(open('db.txt',encoding='utf-8'))
    print('剩余票数是: %s' %data['count'])

# 抢票
def get():
    data=json.load(open('db.txt',encoding='utf-8'))
    if data['count'] > 0:
        data['count']-=1
        time.sleep(random.randint(1,3)) # 模拟网络延迟
        json.dump(data,open('db.txt','w',encoding='utf-8'))
        print('%s 购票成功' %os.getpid())

# 把上面两个功能放在task功能中
def task(lock): # 互斥锁：比如合租使用厕所，厕所有门。进去就锁上，否则别人进去就做你身上了。
    # lock.acquire() # 加锁
    # search() # 不能放在里面，这样和join一样。
    # get()
    # lock.release() # 释放锁，容易忘记释放锁。此功能支持上下文管理，使用with会自动调acquire和release。

    # with lock: # 简便写法
    #     search()
    #     get()

    search() # 把它拿出来，别所在里面。大家就都能查票了。
    lock.acquire()
    get()
    lock.release()

if __name__ == '__main__':
    lock=Lock() # 只能 acuquire 一次
    for i in range(10):
        p=Process(target=task,args=(lock,))
        p.start()
        # p.join() # 如果join住就是串行执行了，这么做不合理。其他人连票都看不到。使用互斥锁解决此问题。




# mutex(互斥)一定要传给子进程
# 互斥锁：比如合租使用厕所，厕所有门。进去就锁上，否则别人进去就做你身上了。
from multiprocessing import Process,Lock
import json
import time
import random
import os

lock=Lock() # 全局变量Lock()方法

def search():
    data=json.load(open('db.txt',encoding='utf-8'))
    print('剩余票数是: %s' %data['count'])

def get():
    data=json.load(open('db.txt',encoding='utf-8'))
    if data['count'] > 0:
        data['count']-=1
        time.sleep(random.randint(1,3)) # 模拟网络延迟
        json.dump(data,open('db.txt','w',encoding='utf-8'))
        print('%s 购票成功' %os.getpid())

def task():
    search()
    lock.acquire()
    get()
    lock.release()


if __name__ == '__main__':
    for i in range(10):
        p=Process(target=task) # args=(lock,)互斥锁一定要传给子进程，否则会一人拿到一把锁。
        p.start()

# 完整互斥锁代码
from multiprocessing import Process,Lock
import json
import time
import random
import os

lock=Lock()

def search():
    data=json.load(open('db.txt',encoding='utf-8'))
    print('剩余票数是: %s' %data['count'])

def get():
    data=json.load(open('db.txt',encoding='utf-8'))
    if data['count'] > 0:
        data['count']-=1
        time.sleep(random.randint(1,3)) # 模拟网络延迟
        json.dump(data,open('db.txt','w',encoding='utf-8'))
        print('%s 购票成功' %os.getpid())

def task(lock):
    search()
    lock.acquire()
    get()
    lock.release()


if __name__ == '__main__':
    for i in range(10):
        p=Process(target=task,args=(lock,)) 
        p.start()


# 总结: join是把整体串行,Lock是把局部串行。

# 加锁可以保证多个进程修改同一块数据时，同一时间只能有一个任务可以进行修改，即串行的修改，没错，速度是慢了，但牺牲了速度却保证了数据安全。
虽然可以用文件共享数据实现进程间通信，但问题是：
1.效率低（共享数据基于文件，而文件是硬盘上的数据）
2.需要自己加锁处理

# 因此我们最好找寻一种解决方案能够兼顾：1、效率高（多个进程共享一块内存的数据）2、帮我们处理好锁问题。这就是mutiprocessing模块为我们提供的基于消息的IPC通信机制：队列和管道。
1 队列和管道都是将数据存放于内存中
2 队列又是基于（管道+锁）实现的，可以让我们从复杂的锁问题中解脱出来，我们应该尽量避免使用共享数据，尽可能使用消息传递和队列，避免处理复杂的同步和锁问题，而且在进程数目增多时，往往可以获得更好的可获展性。