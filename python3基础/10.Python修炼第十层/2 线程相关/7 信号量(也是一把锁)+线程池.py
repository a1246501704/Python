'''
信号量Semaphore
同进程的一样
Semaphore管理一个内置的计数器，
每当调用acquire()时内置计数器-1；
调用release() 时内置计数器+1；
计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()。

实例：(同时只有5个线程可以获得semaphore,即可以限制最大连接数为5)
与进程池是完全不同的概念，进程池Pool(4)，最大只能产生4个进程，而且从头到尾都只是这四个进程，不会产生新的，而信号量是产生一堆线程/进程
'''

'''
信号量是一次性开启多个线程(例如20个)
限制信号量的数量为5个，同时有5个在运行，控制5个5个的执行
进程池和线程池 的概念是 从始至终就是这个数量的进程或线程在运行
'''
# 就想公共厕所有5个坑，门口有5把钥匙。进去一个人就拿一把。其他人等着。
from threading import Thread,Semaphore,current_thread
import time,random

sm=Semaphore(5) # 5个人先抢到锁，第六个人等着。等有人出来。
def task():
    # sm.acquire()
    # print('%s 正在上厕所' %current_thread().getName())
    # time.sleep(random.randint(1,3))
    # sm.release()
    with sm: # 也支持with上下文管理
        print('%s 正在上厕所' %current_thread().getName())
        time.sleep(random.randint(1,3))

if __name__ == '__main__':
    for i in range(20): # 模拟有20个人要上厕所。先产生了20线程，控制5个5个的执行。
        t=Thread(target=task)
        t.start()
'''信号量是一次性开启多个线程，上厕所的过程是 出来几个。再进去几个。
Thread-1 正在上厕所
Thread-2 正在上厕所
Thread-3 正在上厕所
Thread-4 正在上厕所
Thread-5 正在上厕所

Thread-6 正在上厕所

Thread-9 正在上厕所
Thread-8 正在上厕所
Thread-10 正在上厕所
Thread-7 正在上厕所


Thread-12 正在上厕所
Thread-11 正在上厕所
Thread-13 正在上厕所


Thread-14 正在上厕所
Thread-15 正在上厕所


Thread-16 正在上厕所
Thread-17 正在上厕所


Thread-18 正在上厕所
Thread-19 正在上厕所
Thread-20 正在上厕所
'''


# 和线程池的区别
from threading import Thread,Semaphore,current_thread
from concurrent.futures import ThreadPoolExecutor
import time,random

def task(id):
    print('%s 正在上厕所 %s' %(current_thread().getName(),id))
    time.sleep(random.randint(1,3))

if __name__ == '__main__':
    t=ThreadPoolExecutor(5) # 如果不指定线程池的大小，默认是cpu核心数的5倍。
    for i in range(20):
        t.submit(task,i)
    # t.map(task,range(20)) # # map是个简单的方法，可以替代for循环。task函数还是要要接收id，但是这里默认就已经传了。

    t.shutdown(wait=True)
'''始终都是5个线程在干活，执行过程中回车断开看着比较明显。
ThreadPoolExecutor-0_0 正在上厕所 1
ThreadPoolExecutor-0_1 正在上厕所 2
ThreadPoolExecutor-0_2 正在上厕所 3
ThreadPoolExecutor-0_3 正在上厕所 4
ThreadPoolExecutor-0_4 正在上厕所 5

ThreadPoolExecutor-0_4 正在上厕所 6

ThreadPoolExecutor-0_1 正在上厕所 7
ThreadPoolExecutor-0_2 正在上厕所 8
ThreadPoolExecutor-0_3 正在上厕所 9
ThreadPoolExecutor-0_0 正在上厕所 10

ThreadPoolExecutor-0_4 正在上厕所 11
ThreadPoolExecutor-0_2 正在上厕所 12
ThreadPoolExecutor-0_3 正在上厕所 13
ThreadPoolExecutor-0_0 正在上厕所 14

ThreadPoolExecutor-0_2 正在上厕所 15
ThreadPoolExecutor-0_0 正在上厕所 16
ThreadPoolExecutor-0_4 正在上厕所 17

ThreadPoolExecutor-0_1 正在上厕所 18
ThreadPoolExecutor-0_3 正在上厕所 19
ThreadPoolExecutor-0_2 正在上厕所 20
'''