\一 multiprocessing模块介绍
python中的多线程无法利用多核优势，如果想要充分地使用多核CPU的资源（os.cpu_count()查看），在python中大部分情况需要使用多进程。Python提供了multiprocessing。
    multiprocessing模块用来开启子进程，并在子进程中执行我们定制的任务（比如函数），该模块与多线程模块threading的编程接口类似。
　  multiprocessing模块的功能众多：支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。
    需要再次强调的一点是：与线程不同，进程没有任何共享状态，进程修改的数据，改动仅限于该进程内。

\二 Process类的介绍
# 创建进程的类：
Process([group [, target [, name [, args [, kwargs]]]]])，由该类实例化得到的对象，表示一个子进程中的任务（尚未启动）
强调：
1. 需要使用关键字的方式来指定参数
2. args指定的为传给target函数的位置参数，是一个元组形式，必须有逗号

# 参数介绍：
group参数未使用，值始终为None
target表示调用对象，即子进程要执行的任务
args表示调用对象的位置参数元组，args=(1,2,'egon',)
kwargs表示调用对象的字典,kwargs={'name':'egon','age':18}
name为子进程的名称

# 方法介绍：
p.start()：启动进程，并调用该子进程中的p.run() 
p.run():进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法  
p.terminate():强制终止进程p，不会进行任何清理操作，如果p创建了子进程，该子进程就成了僵尸进程，使用该方法需要特别小心这种情况。如果p还保存了一个锁那么也将不会被释放，进而导致死锁
p.is_alive():如果p仍然运行，返回True
p.join([timeout]):主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。timeout是可选的超时时间，需要强调的是，p.join只能join住start开启的进程，而不能join住run开启的进程

#  属性介绍：
p.daemon：默认值为False，如果设为True，代表p为后台运行的守护进程，当p的父进程终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程，必须在p.start()之前设置
p.name:进程的名称
p.pid：进程的pid
p.exitcode:进程在运行时为None、如果为–N，表示被信号N结束(了解即可)
p.authkey:进程的身份验证键,默认是由os.urandom()随机生成的32字符的字符串。这个键的用途是为涉及网络连接的底层进程间通信提供安全性，这类连接只有在具有相同的身份验证键时才能成功（了解即可）


\开启进程的两种方式
##开启进程的方式一： 使用函数
from multiprocessing import Process  # Process 的P是大写的
import time,random

def piao(name):
    print('%s is piaoing' %name)
    time.sleep(random.randint(1,3))
    print('%s is over' % name)


if __name__ == '__main__':
    # p=Process(target=piao,kwargs={'name':'alex'}) # 这个方式是按照位置传
    p=Process(target=piao,args=('alex',)) #必须加,号
    p.start() #仅仅只是向操作系统发送了一个创建子进程p的信号，主进程并不会在这里等待子进程执行完再执行下面的代码，等子进程都执行完了主进程才结束。
    print('主')
'''
主
alex is piaoing
alex is over
'''


import time
import random
from multiprocessing import Process
def piao(name):
    print('%s piaoing' %name)
    time.sleep(random.randrange(1,5))
    print('%s piao end' %name)


p1=Process(target=piao,args=('egon',)) #必须加,号
p2=Process(target=piao,args=('alex',))
p3=Process(target=piao,args=('wupeqi',))
p4=Process(target=piao,args=('yuanhao',))

p1.start()# 并不是谁先start就是谁先执行，这只是提交给操作系统一个请求。由操作系统决定。
p2.start()
p3.start()
p4.start()
print('主线程')


##开启进程的方式二： 使用类
from multiprocessing import Process
import time,random

class MyProcess(Process):
    def __init__(self,name): # 如果使用MyProcess类实例化时要传参数就需要实现__init__方法
        super(MyProcess,self).__init__()  # 需要将父类的__init__带过来
        self.name=name

    def run(self): # 必须叫run
        print('%s is piaoing' %self.name)
        time.sleep(random.randint(1,3))
        print('%s is over' % self.name)


if __name__ == '__main__':
    p=MyProcess('P1') 
    p.start() # 仅仅只是向操作系统发送了一个创建子进程p的信号、start会自动调用run
    print('主')
'''
主
P1 is piaoing
P1 is over
'''




import time
import random
from multiprocessing import Process


class Piao(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('%s piaoing' %self.name)

        time.sleep(random.randrange(1,5))
        print('%s piao end' %self.name)

p1=Piao('egon')
p2=Piao('alex')
p3=Piao('wupeiqi')
p4=Piao('yuanhao')

p1.start() #start会自动调用run
p2.start()
p3.start()
p4.start()
print('主线程')