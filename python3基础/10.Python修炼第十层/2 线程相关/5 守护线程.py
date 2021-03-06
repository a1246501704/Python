# 无论是进程还是线程，都遵循：守护xxx会等待主xxx运行完毕后被销毁。需要强调的是：运行完毕并非终止运行。
    #1.对主进程来说，运行完毕指的是主进程代码运行完毕。
    #2.对主线程来说，运行完毕指的是主线程所在的进程内所有非守护线程统统运行完毕，主线程才算运行完毕。

# 详细解释：
    #1 主进程在其代码结束后就已经算运行完毕了（守护进程在此时就被回收）,然后主进程会一直等非守护的子进程都运行完毕后回收子进程的资源(否则会产生僵尸进程)，才会结束。
    #2 主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收）。因为主线程的结束意味着进程的结束，进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束。


# 进程内所有的非守护线程都结束了，主线程（主进程）就结束。不等守护线程。
from threading import Thread
import os
import time
import random

def task():
    print('%s is runing' %os.getpid())
    time.sleep(random.randint(1,3))
    print('%s is done' %os.getpid())


if __name__ == '__main__':
    t=Thread(target=task,)
    t.daemon=True
    t.start()
    print('主') # 在守护线程在sleep时，cpu切到了主线程上执行完退出了。
'''
20296 is runing
主
'''

# 迷惑人的例子
from threading import Thread
import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")# 可以到执行它是因为非守护线程还没执行完。

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    t1=Thread(target=foo)
    t2=Thread(target=bar)

    t1.daemon=True 
    t1.start()  # 守护线程
    t2.start()  # 非守护线程
    print("main-------")
'''
123
456
main-------
end123
end456
'''

from threading import Thread
import time
def foo():
    print(123)
    time.sleep(4)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456") # 当非守护线程都执行完了，守护线程还没执行完也直接结束了。

if __name__ == '__main__':
    t1=Thread(target=foo)
    t2=Thread(target=bar)

    t1.daemon=True 
    t1.start()  # 守护线程
    t2.start()  # 非守护线程
    print("main-------")
'''
123
456
main-------
end456
'''