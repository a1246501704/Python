# 生产者消费者模型
    # 在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。该模式通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度。

# 为什么要使用生产者和消费者模式
    # 在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，
    # 那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。

# 什么是生产者消费者模式
    # 生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，
    # 所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。

\案例: 吃包子典故：厨师造包子（生产者）、筐子装包子（包子队列）、顾客吃包子（消费者）

\没使用队列时的是实现方式
import time

def producer():
    for i in range(10):
        res='包子%s' %i
        consumer(res) # 直接传给了消费者，执行效果是串行。

def consumer(res):
    print(res)
    time.sleep(0.2)

producer()

\基于生产者消费者模型，使用队列实现。
from multiprocessing import Process,Queue
import time
import  random

def producer(name,food,q):
    for i in range(2):
        res = '%s%s' %(food,i)
        time.sleep(random.randint(1,3))
        q.put(res)
        print('%s 生产了 %s' %(name,res))


def consumer(name,q):
    while True:
        res=q.get()
        if res is None:break
        time.sleep(random.randint(1,3))
        print('%s 吃了 %s' %(name,res))

if __name__ == '__main__':
    q=Queue()
    p1=Process(target=producer,args=('egon','包子',q))

    c1=Process(target=consumer,args=('alex',q))

    p1.start()
    c1.start()
'''会一直卡在消费者取数据
egon 生产了 包子0
egon 生产了 包子1
alex 吃了 包子0
alex 吃了 包子1


'''

# 优化
from multiprocessing import Process,Queue
import time
import random

# 生产者
def producer(name,food,q):
    for i in range(2):
        res='%s%s' %(food,i)
        time.sleep(random.randint(1,3))
        q.put(res)
        print('%s 生产了 %s' %(name,res))
    # q.put(None) # 如果有多个消费者会出错，队列中间会有None。

# 消费者
def consumer(name,q):
    while True:
        res=q.get()
        if res is None:break # 生产者最后生产了个None，消费者判断并结束循环。
        time.sleep(random.randint(1, 3))
        print('%s 吃了 %s' %(name,res))

if __name__ == '__main__':
    q=Queue()
    # 多个生产者
    p1=Process(target=producer,args=('egon','包子',q))
    p2=Process(target=producer,args=('贱哥','骨头',q))
    # 多个消费者
    c1=Process(target=consumer,args=('alex',q))
    c2=Process(target=consumer,args=('alex',q))
    c3=Process(target=consumer,args=('alex',q))

    # 启动生产者
    p1.start()
    p2.start()
    # 启动消费者
    c1.start()
    c2.start()
    c3.start()

    p1.join() # 必须保证生产者全部生产完毕,才应该发送结束信号。把生产者join住，保证生产完在加入None。
    p2.join()
    q.put(None) # 发送结束信号。多个消费者时，生产者生产完了往队列最后放入几个None，给三个消费者每人一个None。方法很low，有几个消费者就要传一个None。
    q.put(None)
    q.put(None)
# 此时的问题是主进程永远不会结束，原因是：生产者p在生产完后就结束了，但是消费者c在取空了q之后，则一直处于死循环中且卡在q.get()这一步。
# 解决方式无非是让生产者在生产完毕后，往队列中再发一个结束信号(None)，这样消费者在接收到结束信号后就可以break出死循环。


# 异常处理和get_nowait()方案不可行
from multiprocessing import Process,Queue
import time
import random

def producer(name,food,q):
    for i in range(10):
        res='%s%s' %(food,i)
        time.sleep(random.randint(1,3))
        q.put(res)
        print('%s 生产了 %s' %(name,res))

def consumer(name,q):
    while True:
        try:
            res=q.get_nowait() # 生产者还没往队列放数据呢，啥都取不到。直接结束了。
            time.sleep(random.randint(1, 3))
            print('%s 吃了 %s' %(name,res))
        except Exception:
            break

if __name__ == '__main__':
    q=Queue()
    p1=Process(target=producer,args=('egon','泔水',q))

    c1=Process(target=consumer,args=('alex',q))


    p1.start()
    c1.start()


\由消费者发通知，说它确实收到了数据。使用JoinableQueue方法
#JoinableQueue([maxsize])：这就像是一个Queue对象，但队列允许项目的使用者通知生成者项目已经被成功处理。通知进程是使用共享的信号和条件变量来实现的。
   #参数介绍：
    maxsize是队列中允许最大项数，省略则无大小限制。    
　 #方法介绍：
    JoinableQueue的实例p除了与Queue对象相同的方法之外还具有:
    q.task_done(): 使用者使用此方法发出信号，表示q.get()的返回项目已经被处理。如果调用此方法的次数大于从队列中删除项目的数量，将引发ValueError异常
    q.join(): 生产者调用此方法进行阻塞，直到队列中所有的项目均被处理。阻塞将持续到队列中的每个项目均调用q.task_done（）方法为止

from multiprocessing import Process,Queue,JoinableQueue
import time
import random

def producer(name,food,q):
    for i in range(3):
        res='%s%s' %(food,i)
        time.sleep(random.randint(1,3))
        q.put(res)
        print('%s 生产了 %s' %(name,res))

def consumer(name,q):
    while True:
        res=q.get()
        if res is None:break
        time.sleep(random.randint(1, 3))
        print('%s 吃了 %s' %(name,res))
        q.task_done() # 向q.join()发送一次信号,证明一个数据已经被取走了。计数减一

if __name__ == '__main__':
    q=JoinableQueue() #可以调q.join()方法，join住q，q的数据被取完就结束了。
    
    #生产者们:即厨师们
    p1=Process(target=producer,args=('egon','馒头',q))
    p2=Process(target=producer,args=('贱哥','大饼',q))
    
    #消费者们:即吃货们
    c1=Process(target=consumer,args=('alex',q))
    c2=Process(target=consumer,args=('alex',q))
    c3=Process(target=consumer,args=('alex',q))

    c1.daemon=True # 把消费者变为守护进程，当q.join执行结束时已经确定生产者都生产完了，消费者已经消费完了。所以消费者也可以退出了。如果不把消费者设置成守护进程，消费者还在get数据。
    c2.daemon=True
    c3.daemon=True

    # p1.start()
    # p2.start()

    # c1.start()
    # c2.start()
    # c3.start()
    #开始
    p_l=[p1,p2,p3,c1,c2]
    for p in p_l:
        p.start()

    p1.join()
    p2.join()

    q.join() # 取到队列中数据计数。上面的start执行完会直接到此行代码，还没消费就结束了。所以要把p1和p2都join住。保证生产完毕再q.join住才有意义。
    print('主')
# 主进程等--->p1,p2,p3等---->c1,c2
# p1,p2,p3结束了,证明c1,c2肯定全都收完了p1,p2,p3发到队列的数据
# 因而c1,c2也没有存在的价值了,应该随着主进程的结束而结束,所以设置成守护进程


\生产者消费者模型总结
    # 程序中有两类角色
        一类负责生产数据（生产者）
        一类负责处理数据（消费者）
    # 引入生产者消费者模型为了解决的问题是：
        平衡生产者与消费者之间的工作能力，从而提高程序整体处理数据的速度。
    # 如何实现：
        生产者<-->队列<——>消费者
    # 生产者消费者模型实现类程序的解耦和







