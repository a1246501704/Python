# 进程彼此之间互相隔离，要实现进程间通信（IPC），multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的。

# 创建队列的类（底层就是以管道和锁定的方式实现):
#     Queue([maxsize]):创建共享的进程队列，Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。 

# 参数介绍:
#     maxsize是队列中允许最大项数，省略则无大小限制。 

# 方法介绍: 比如q为队列
    # q.put: 方法用以插入数据到队列中，put方法还有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。如果超时，会抛出Queue.Full异常。如果blocked为False，但该Queue已满，会立即抛出Queue.Full异常。
    # q.get: 方法可以从队列读取并且删除一个元素。同样，get方法有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，会抛出Queue.Empty异常。如果blocked为False，有两种情况存在，如果Queue有一个值可用，则立即返回该值，否则，如果队列为空，则立即抛出Queue.Empty异常.
    # q.get_nowait():同q.get(False)
    # q.put_nowait():同q.put(False)
    # q.empty(): 调用此方法时q为空则返回True，该结果不可靠，比如在返回True的过程中，如果队列中又加入了项目。
    # q.full(): 调用此方法时q已满则返回True，该结果不可靠，比如在返回True的过程中，如果队列中的项目被取走。
    # q.qsize(): 返回队列中目前项目的正确数量，结果也不可靠，理由同q.empty()和q.full()一样。

# 其他方法(了解):
    # q.join() 实际上意味着等到队列为空，再执行别的操作
    # q.cancel_join_thread():不会在进程退出时自动连接后台线程。可以防止join_thread()方法阻塞
    # q.close():关闭队列，防止队列中加入更多数据。调用此方法，后台线程将继续写入那些已经入队列但尚未写入的数据，但将在此方法完成时马上关闭。如果q被垃圾收集，将调用此方法。关闭队列不会在队列使用者中产生任何类型的数据结束信号或异常。例如，如果某个使用者正在被阻塞在get()操作上，关闭生产者中的队列不会导致get()方法返回错误。
    # q.join_thread()：连接队列的后台线程。此方法用于在调用q.close()方法之后，等待所有队列项被消耗。默认情况下，此方法由不是q的原始创建者的所有进程调用。调用q.cancel_join_thread方法可以禁止这种行为


from multiprocessing import Process,Queue

q=Queue(3) # 队列大小

q.put({'count':10}) # 放入队列的第一个数据
q.put('a') # 放入队列的第二个数据
q.put('1') # 放入队列的第三个数据
# q.put(2) # 第四个放不进去了，会卡住。
# q.put_nowait(2) # 不等待，证明队列满了。可以用try捕捉这个异常，避免程序因放不进队列而阻塞。


print(q.get()) # 查看数据1
print(q.get()) # 查看数据2
print(q.get()) # 查看数据3
# print(q.get()) # 第四个也不能取
print(q.get_nowait())



# 应用:
'''
multiprocessing模块支持进程间通信的两种主要形式:管道和队列
都是基于消息传递实现的,但是队列接口
'''

from multiprocessing import Process,Queue
import time
q=Queue(3) # 队列大小

#put ,get ,put_nowait,get_nowait,full,empty
q.put(3)
q.put(3)
q.put(3)
print(q.full()) # 满了

print(q.get())
print(q.get())
print(q.get())
print(q.empty()) # 空了









