\查看进程id
import os,time
print(os.getpid())  #自己的进程的pid
print(os.getppid()) #自己的父进程的pid
time.sleep(1000)
'''
45496
334
'''


from multiprocessing import Process,Pool
import time,random
import os

def task():
    print('%s is running parent[%s]' %(os.getpid(),os.getppid())) 

if __name__ == '__main__':
    p=Process(target=task)
    p.start()
    print(p.pid)            #p这个子进程的id 和进程里的os.getpid()是一样的功能
    print('主',os.getpid()) #查看当前执行文件.py的id
    print(os.getppid())     #pycharm的进程id（因为当前文件是用pycharm执行的）、如果在cmd里执行getppid就是cmd
    time.sleep(1000)
'''
45483
主 45482
334
45483 is running parent[45482]
'''



\terminate（终止） + is_alive（是否存活）
#进程对象的其他方法一:terminate,is_alive
from multiprocessing import Process,Pool
import time,random
import os

def task():
    print('%s is running' %(os.getpid()))
    time.sleep(10)

if __name__ == '__main__':
    p=Process(target=task)
    p.start()
    p.terminate()       # 给操作系统发了一个杀死子进程的信号，这个操作少用。万一task里也开启了子进程了，父进程被杀死后子进程就成僵尸进程了。
    time.sleep(1)       # 给操作系统去杀死子进程的时间，否则立马看is_alive还会是True
    print(p.is_alive()) # 判断子进程是否存活
    print('主')
'''
False
主
'''

from multiprocessing import Process
import time
import random

class Piao(Process):
    def __init__(self,name):
        self.name=name
        super().__init__()

    def run(self):
        print('%s is piaoing' %self.name)
        time.sleep(random.randrange(1,5))
        print('%s is piao end' %self.name)


p1=Piao('egon1')
p1.start()

p1.terminate()       #关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活
print(p1.is_alive()) #结果为True

print('开始')
print(p1.is_alive()) #结果为False



\name与pid
from multiprocessing import Process,Pool
import time,random
import os

def task():
    print('%s is running' %(os.getpid()))
    time.sleep(10)

if __name__ == '__main__':
    p=Process(target=task)
    p.start()
    print(p.name)  # 默认子进程 Process-1 命名
    print('主')
'''
Process-1
主
45648 is running
'''

from multiprocessing import Process,Pool
import time,random
import os

def task():
    print('%s is running' %(os.getpid()))
    time.sleep(10)

if __name__ == '__main__':
    p=Process(target=task,name='xxxxxxxxxxxx')  # 给子进程指定名字
    p.start()
    print(p.name)
    print('主')
'''
xxxxxxxxxxxx
主
45644 is running
'''

from multiprocessing import Process
import time
import random
class Piao(Process):
    def __init__(self,name):
        # self.name=name
        # super().__init__() #Process的__init__方法会执行self.name=Piao-1,
        #                    #所以加到这里,会覆盖我们的self.name=name

        #为我们开启的进程设置名字的做法
        super().__init__()
        self.name=name

    def run(self):
        print('%s is piaoing' %self.name)
        time.sleep(random.randrange(1,3))
        print('%s is piao end' %self.name)

p=Piao('egon')
p.start()
print('开始')
print(p.pid) #查看pid
'''
开始
45688
egon is piaoing
egon is piao end
'''