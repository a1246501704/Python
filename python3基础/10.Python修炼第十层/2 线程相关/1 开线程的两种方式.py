\1、什么是线程
# 在传统操作系统中，每个进程有一个地址空间，而且默认就有一个控制线程。线程才是真正的执行单位。
# 线程顾名思义，就是一条流水线工作的过程，一条流水线必须属于一个车间，一个车间的工作过程是一个进程。
# 车间负责把资源整合到一起，是一个资源单位，而一个车间内至少有一个流水线。流水线的工作需要电源，电源就相当于cpu。
# 所以，进程只是用来把资源集中到一起（进程只是一个资源单位，或者说资源集合），而线程才是cpu上的执行单位。
# 多线程（即多个控制线程）的概念是，在一个进程中存在多个控制线程，多个控制线程共享该进程的地址空间，相当于一个车间内有多条流水线，都共用一个车间的资源。
# 例如，北京地铁与上海地铁是不同的进程，而北京地铁里的13号线是一个线程，北京地铁所有的线路共享北京地铁所有的资源，比如所有的乘客可以被所有线路拉。

\2、线程的创建开销小
# 创建进程的开销要远大于线程？ 是的
# 如果我们的软件是一个工厂，该工厂有多条流水线，流水线工作需要电源，电源只有一个即cpu（单核cpu）。一个车间就是一个进程，一个车间至少一条流水线（一个进程至少有一个线程）
# 创建一个进程，就是创建一个车间（申请空间，在该空间内建至少一条流水线），而建线程，就只是在一个车间内造一条流水线，无需申请空间，所以创建开销小。创建一个车间肯定比创建一条流水线要慢。

# 进程之间是竞争关系，线程之间是协作关系？ 是的
# 不同车间之间是竞争/抢电源的关系，竞争（不同的进程直接是竞争关系，是不同的程序员写的程序运行的，迅雷抢占其他进程的网速，360把其他进程当做病毒干死）
# 一个车间的不同流水线式协同工作的关系（同一个进程的线程之间是合作关系，是同一个程序写的程序内开启动，迅雷内的线程是合作关系，不会自己干自己）

\3、线程与进程的区别
# 线程共享进程的地址空间;进程有自己的地址空间。
# 线程可以直接访问其进程的数据段;进程拥有父进程的数据段的自己的副本。
# 线程可以直接与进程中的其他线程通信;进程必须使用进程间通信来与同级进程通信。
# 新线程很容易创建;新进程需要父进程的复制。
# 线程可以对同一进程的线程进行相当大的控制;进程只能对子进程进行控制。
# 主线程的更改(取消、优先级更改等)可能会影响进程中其他线程的行为;对父进程的更改不影响子进程。

\4、为何要用多线程
# 多线程指的是，在一个进程中开启多个线程，简单的讲：如果多个任务共用一块地址空间，那么必须在一个进程内开启多个线程。详细的讲分为4点：
1. 多线程共享一个进程的地址空间
2. 线程比进程更轻量级，线程比进程更容易创建可撤销，在许多操作系统中，创建一个线程比创建一个进程要快10-100倍，在有大量线程需要动态和快速修改时，这一特性很有用
3. 若多个线程都是cpu密集型的，那么并不能获得性能上的增强，但是如果存在大量的计算和大量的I/O处理，拥有多个线程允许这些活动彼此重叠运行，从而会加快程序执行的速度。
4. 在多cpu系统中，为了最大限度的利用多核，可以开启多个线程，比开进程开销要小的多。（这一条并不适用于python）

\5、线程相关的其他方法
# Thread实例对象的方法
  # isAlive(): 返回线程是否活动的。
  # getName(): 返回线程名。
  # setName(): 设置线程名。

# threading模块提供的一些方法：
  # threading.currentThread(): 返回当前的线程变量。
  # threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
  # threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

\使用多线程执行
from threading import Thread # threading包中Thread线程模块
from multiprocessing import Process # multiprocessing包中的Process进程模块
import os
import time
import random

def task():
    print('%s is runing' %os.getpid()) # 线程的pid就是进程的pid
    time.sleep(random.randint(1,3))
    print('%s is done' %os.getpid())

if __name__ == '__main__':
    t=Thread(target=task,) # 开启多线程执行，可以看出线程启动很快，在‘主’还没打印出来就已经执行线程中的代码了。
    t.start()
    print('主',os.getpid())
# 执行结果:
# 46950 is runing
# 主 46950
# 46950 is done

\使用多进程执行
from threading import Thread
from multiprocessing import Process
import os
import time
import random

def task():
    print('%s is runing' %os.getpid())
    time.sleep(random.randint(1,3))
    print('%s is done' %os.getpid())

if __name__ == '__main__':
    t=Process(target=task,) # 开启子进程执行，可以看出主进程执行完才执行的子进程。对比出进程启动比线程慢很多。
    t.start()
    print('主',os.getpid())
# 执行结果:
# 主 46656
# 46658 is runing
# 46658 is done

\使用线程类继承执行
from threading import Thread
from multiprocessing import Process
import os
import time
import random

class Mythread(Thread): # 继承自threading包中的Thread模块.
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('%s is runing' %os.getpid())
        time.sleep(random.randint(1,3))
        print('%s is done' %os.getpid())

if __name__ == '__main__':
    t=Mythread('线程1')
    t.start()
    print('主',os.getpid())

# 执行结果:
# 46630 is runing
# 主 46630
# 46630 is done


\例子（瞅一瞅pid）:
from threading import Thread
from multiprocessing import Process
import os

def work():
    print('hello',os.getpid(),end="\n")

if __name__ == '__main__':
    #part1:在主进程下开启多个线程,每个线程都跟主进程的pid一样
    t1=Thread(target=work)
    t2=Thread(target=work)
    t1.start()
    t2.start()
    print('主线程/主进程pid',os.getpid())

    #part2:开多个进程,每个进程都有不同的pid
    p1=Process(target=work)
    p2=Process(target=work)
    p1.start()
    p2.start()
    print('主线程/主进程pid',os.getpid())

'''
hello 55734
hello 55734
主线程/主进程pid 55734
主线程/主进程pid 55734
hello 55735
hello 55736
'''