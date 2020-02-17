'''
http://www.cnblogs.com/linhaifeng/articles/7449853.html

结论：在Cpython解释器中，同一个进程下开启的多线程，同一时刻只能有一个线程执行，无法利用多核优势。计算密集型多进程可以利用多核优势。
'''
# GIL本质上就是一把互斥锁，系统默认，不可修改。


# \GIL介绍
# GIL本质就是一把互斥锁，既然是互斥锁，所有互斥锁的本质都一样，都是将并发运行变成串行，以此来控制同一时间内共享数据只能被一个任务所修改，进而保证数据安全。
# 可以肯定的一点是：保护不同的数据的安全，就应该加不同的锁。

# \三个需要注意的点：
#1.线程抢的是GIL锁，GIL锁相当于执行权限，拿到执行权限后才能拿到互斥锁Lock，其他线程也可以抢到GIL，但如果发现Lock仍然没有被释放则阻塞，即便是拿到执行权限GIL也要立刻交出来
#2.join是等待所有，即整体串行，而锁只是锁住修改共享数据的部分，即部分串行，要想保证数据安全的根本原理在于让并发变成串行，join与互斥锁都可以实现，毫无疑问，互斥锁的部分串行效率要更高
#3. 一定要看本小节最后的GIL与互斥锁的经典分析

# \GIL VS Lock
#     机智的同学可能会问到这个问题，就是既然你之前说过了，Python已经有一个GIL来保证同一时间只能有一个线程来执行了，为什么这里还需要lock? 
# 　  首先我们需要达成共识：锁的目的是为了保护共享的数据，同一时间只能有一个线程来修改共享的数据
#     然后，我们可以得出结论：保护不同的数据就应该加不同的锁。
# 　  最后，问题就很明朗了，GIL 与Lock是两把锁，保护的数据不一样，前者是解释器级别的（当然保护的就是解释器级别的数据，比如垃圾回收的数据），
# 后者是保护用户自己开发的应用程序的数据，很明显GIL不负责这件事，只能用户自定义加锁处理，即Lock。

# 过程分析：所有线程抢的是GIL锁，或者说所有线程抢的是执行权限
# 　　线程1抢到GIL锁，拿到执行权限，开始执行，然后加了一把Lock，还没有执行完毕，即线程1还未释放Lock，有可能线程2抢到GIL锁，开始执行，
# 执行过程中发现Lock还没有被线程1释放，于是线程2进入阻塞，被夺走执行权限，有可能线程1拿到GIL，然后正常执行到释放Lock。。。这就导致了串行运行的效果
# 　　既然是串行，那我们执行
# 　　t1.start()
# 　　t1.join
# 　　t2.start()
# 　　t2.join()
# 　　这也是串行执行啊，为何还要加Lock呢，需知join是等待t1所有的代码执行完，相当于锁住了t1的所有代码，而Lock只是锁住一部分操作共享数据的代码。

# 详细介绍:
#     因为Python解释器帮你自动定期进行内存回收，你可以理解为python解释器里有一个独立的线程，每过一段时间它起wake up做一次全局轮询看看哪些内存数据是可以
#     被清空的，此时你自己的程序 里的线程和 py解释器自己的线程是并发运行的，假设你的线程删除了一个变量，py解释器的垃圾回收线程在清空这个变量的过程中的clearing时刻，
#     可能一个其它线程正好又重新给这个还没来及得清空的内存空间赋值了，结果就有可能新赋值的数据被删除了，为了解决类似的问题，python解释器简单粗暴的加了锁，即当一个线程运行时，
#     其它人都不能动，这样就解决了上述的问题，这可以说是Python早期版本的遗留问题。

import os
import time
print(os.getpid()) 
# 是python解释器的进程id，实际上python的代码无法执行，python解释器是用c语言写的，python解释器将我们写的python代码当作参数传给c语言去执行。
time.sleep(1000)


# 计算密集型（多进程效率高）
from multiprocessing import Process
from threading import Thread
import os,time

def work():
    res=0
    for i in range(10000): # 模拟计算操作
        res *= i

if __name__ == '__main__':
    l=[]
    print(os.cpu_count()) # 本机为4核
    start=time.time()
    for i in range(4):
        p=Process(target=work) # 8.546488761901855
        # p=Thread(target=work)    # 20.968199253082275
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop=time.time()
    print('run time is %s' %(stop-start))


# I/O密集型（多线程效率高）
from multiprocessing import Process
from threading import Thread
import threading
import os,time

def work():
    time.sleep(2) # 模拟io延迟


if __name__ == '__main__':
    l=[]
    print(os.cpu_count()) # 本机为4核
    start=time.time()
    for i in range(4):
        # p=Process(target=work)  # 2.2081263065338135
        p=Thread(target=work) # 2.0041143894195557
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop=time.time()
    print('run time is %s' %(stop-start))


# 锁通常被用来实现对共享资源的同步访问。为每一个共享资源创建一个Lock对象，当你需要访问该资源时，调用acquire
# 方法来获取锁对象（如果其它线程已经获得了该锁，则当前线程需等待其被释放），待资源访问完后，再调用release方法释放锁：
'''
import threading

R=threading.Lock()

R.acquire()
'''
对公共数据的操作
'''
R.release()
'''

# 实例
from threading import Thread,Lock
import os,time

def work():
    global n
    lock.acquire()
    temp=n
    time.sleep(0.1)
    n=temp-1
    lock.release()

if __name__ == '__main__':
    lock=Lock()
    n=100
    l=[]
    for i in range(100):
        p=Thread(target=work)
        l.append(p)
        p.start()
    for p in l:
        p.join()

    print(n) #结果肯定为0，由原来的并发执行变成串行，牺牲了执行效率保证了数据安全

\GIL锁与互斥锁总和分析：
　　 #1. 100个线程去抢GIL锁，即抢执行权限
    #2. 肯定有一个线程先抢到GIL（暂且称为线程1），然后开始执行，一旦执行就会拿到lock.acquire()
    #3. 极有可能线程1还未运行完毕，就有另外一个线程2抢到GIL，然后开始运行，但线程2发现互斥锁lock还未被线程1释放，于是阻塞，被迫交出执行权限，即释放GIL。
    #4. 直到线程1重新抢到GIL，开始从上次暂停的位置继续执行，直到正常释放互斥锁lock，然后其他的线程再重复2 3 4的过程。

\互斥锁与join的区别：
#不加锁:并发执行,速度快,数据不安全。数据乱了
from threading import current_thread,Thread,Lock
import os,time

def task():
    global n
    print('%s is running' %current_thread().getName()) # 获取进程名称
    temp=n
    time.sleep(0.5)
    n=temp-1

if __name__ == '__main__':
    n=100
    lock=Lock()
    threads=[]
    start_time=time.time()
    for i in range(100):
        t=Thread(target=task)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    stop_time=time.time()
    print('主:%s n:%s' %(stop_time-start_time,n))

'''
Thread-1 is running
Thread-2 is running
......
Thread-100 is running
主:0.5216062068939209 n:99 
'''


#不加锁:未加锁部分并发执行,加锁部分串行执行,速度慢,数据安全
from threading import current_thread,Thread,Lock
import os,time
def task():
    #未加锁的代码并发运行
    time.sleep(3)
    print('%s start to run' %current_thread().getName())
    global n
    #加锁的代码串行运行
    lock.acquire()
    temp=n
    time.sleep(0.5)
    n=temp-1
    lock.release()

if __name__ == '__main__':
    n=100
    lock=Lock()
    threads=[]
    start_time=time.time()
    for i in range(100):
        t=Thread(target=task)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    stop_time=time.time()
    print('主:%s n:%s' %(stop_time-start_time,n))

'''
Thread-1 is running
Thread-2 is running
......
Thread-100 is running
主:53.294203758239746 n:0
'''

# 有的同学可能有疑问:既然加锁会让运行变成串行,那么我在start之后立即使用join,就不用加锁了啊,也是串行的效果啊
# 没错:在start之后立刻使用join,肯定会将100个任务的执行变成串行,毫无疑问,最终n的结果也肯定是0,是安全的,但问题是
# start后立即join:任务内的所有代码都是串行执行的,而加锁,只是加锁的部分即修改共享数据的部分是串行的
# 单从保证数据安全方面,二者都可以实现,但很明显是加锁的效率更高.
from threading import current_thread,Thread,Lock
import os,time
def task():
    time.sleep(3)
    print('%s start to run' %current_thread().getName())
    global n
    temp=n
    time.sleep(0.5)
    n=temp-1


if __name__ == '__main__':
    n=100
    lock=Lock()
    start_time=time.time()
    for i in range(100):
        t=Thread(target=task)
        t.start()
        t.join() # 串行
    stop_time=time.time()
    print('主:%s n:%s' %(stop_time-start_time,n))

'''
Thread-1 start to run
Thread-2 start to run
......
Thread-100 start to run
主:350.6937336921692 n:0 # 耗时是多么的恐怖
'''