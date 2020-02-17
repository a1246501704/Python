# 守护进程，下面是个不合理使用守护进程的例子
from multiprocessing import Process
import os
import time

def task():
    print('%s is ruuning' %os.getpid())
    time.sleep(3)
    print('%s is done' % os.getpid())


if __name__ == '__main__':
    p=Process(target=task,)
    p.daemon = True # 把p变成一个守护进程（太监），必须在p.start()前设置。主进程一结束，守护进程也跟着退出。
    p.start()
    time.sleep(1)
    # p.join() # 等着子进程结束完再执行其他，这样设置守护进程就没意义了。
    print('主') # 主（皇帝）运行结束后，守护进程还没干完活就退出了。如果没有daemon守护进程的话，主会等着子结束再结束。

    #什么时候用守护进程？
        # 首先开子进程的目的就是为了并发执行任务，如果说该任务的执行周期与主进程的执行周期是一致的，那么必须把该任务的进程设置为守护进程。


# 迷惑人的例子（主进程代码运行完毕,守护进程就会结束）
from multiprocessing import Process
import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':

    p1=Process(target=foo)
    p2=Process(target=bar)

    p1.daemon=True
    p1.start()
    p2.start() # 还要等p2执行完，主才结束。p2的地位比p1高。
    print("main-------") #打印该行则主进程代码结束,则守护进程p1应该被终止,可能会有p1任务执行的打印信息123,因为主进程打印main----时,p1也执行了,但是随即被终止


    #1:守护进程到底什么时候死？：下面2做完
    #2：主进程到底什么时候算执行完毕：主进程运行完毕最后一行代码
    #3：主进程什么时候应该死掉：等到所有的非守护的子进程都死掉，主才死
    #4：主进程执行完毕了，是否意味着主进程会立马死掉？ 否



# 守护进程内不能再开子进程
# 子进程内可以再开子进程
from multiprocessing import Process
import os
import time

def foo():
    print('%s is ruuning' %os.getpid())
    time.sleep(3)
    print('%s is done' % os.getpid())

def task():
    print('%s is ruuning' %os.getpid())
    time.sleep(3)
    print('%s is done' % os.getpid())

    p=Process(target=foo) # 也启动了一个子进程,运行时会报错。守护的进程是允许有儿子的。
    # p.daemon=True # 不可以使用
    p.start()

if __name__ == '__main__':
    p=Process(target=task,)
    p.daemon = True # 必须在p.start()前设置
    p.start()
    p.join()
    print('主')