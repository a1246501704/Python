
\1. 概述
concurrent.futures 是 3.2 中引入的新模块，它为异步执行可调用对象提供了高层接口。
可以使用 ThreadPoolExecutor 来进行多线程编程，ProcessPoolExecutor 进行多进程编程，两者实现了同样的接口，这些接口由抽象类 Executor 定义。
这个模块提供了两大类型，一个是执行器类 Executor，另一个是 Future 类。
执行器用来管理工作池，future 用来管理工作计算出来的结果，通常不用直接操作 future 对象，因为有丰富的 API。

\2. Executor Object 执行器对象
concurrent.futures.Executor 类，这个抽象类提供了一系列方法，可以用于异步执行调用。它不能直接使用，只能通过子类化出来的具体类来使用。

它定义的方法有：
# submit(fn, *args, **kwargs)
安排可调用对象 fn 以 fn(*args, **kwargs) 的形式执行，并返回 Future 对象来表示它的执行。

with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pow, 323, 1235)
    print(future.result())

# map(func, *iterables, timeout=None, chunksize=1)
类似内置函数 map(func, *iterables)，但是有两点不同：
    1.立即获取 iterables 而不会惰性获取；
    2.异步执行 func，并支持多次并发调用。
它返回一个迭代器。
从调用 Executor.map() 开始的 timeout 秒之后，如果在迭代器上调用了 __next__() 并且无可用结果的话，迭代器会抛出 concurrent.futures.TimeoutError 异常。
timeout 秒数可以是浮点数或者整数，如果设置为 None 或者不指定，则不限制等待时间。

如果 func 调用抛出了异常，那么该异常会在从迭代器获取值的时候抛出。

当使用 ProcessPoolExecutor 的时候，这个方法会把 iterables 划分成多个块，作为独立的任务提交到进程池。这些块的近似大小可以通过给 chunksize 指定一个正整数。对于很长的 iterables，
使用较大的 chunksize 而不是采用默认值 1，可以显著提高性能。对于 ThreadPoolExecutor，chunksize 不起作用。chunksize 是 3.5 加入的新参数。

注意：不管并发任务的执行次序如何，map 总是基于输入顺序来返回值。map 返回的迭代器，在主程序迭代的时候，会等待每一项的响应。

# shutdown(wait=True)
告诉执行器 executor 在当前所有等待的 future 对象运行完毕后，应该释放执行器用到的所有资源。
在 shutdown 之后再调用 Executor.submit() 和 Executor.map() 会报运行时错误 RuntimeError。
如果 wait 为 True，那么这个方法会在所有等待的 future 都执行完毕，并且属于执行器 executor 的资源都释放完之后才会返回。
如果 wait 为 False，本方法会立即返回。属于执行器的资源会在所有等待的 future 执行完毕之后释放。
不管 wait 取值如何，整个 Python 程序在等待的 future 执行完毕之前不会退出。
import shutil
with ThreadPoolExecutor(max_workers=4) as e:
    e.submit(shutil.copy, 'src1.txt', 'dest1.txt')
    e.submit(shutil.copy, 'src2.txt', 'dest2.txt')
    e.submit(shutil.copy, 'src3.txt', 'dest3.txt')
    e.submit(shutil.copy, 'src4.txt', 'dest4.txt')

执行器类 Executor 实现了上下文协议，可以用做上下文管理器。它能并发执行任务，等待它们全部完成。当上下文管理器退出时，自动调用 shutdown() 方法。

\ThreadPoolExecutor 线程池执行器
ThreadPoolExecutor 线程池执行器是 Executor 执行器的子类，通过线程池来执行异步调用。它管理一组工作线程，当工作线程有富余的时候，给它们传递任务。
当属于一个 Future 对象的可调用对象等待另一个 Future 的返回时，会发生死锁 deadlock。
举个例子：
import time
def wait_on_b():
    time.sleep(5)
    print(b.result())  # b will never complete because it is waiting on a.
    return 5

def wait_on_a():
    time.sleep(5)
    print(a.result())  # a will never complete because it is waiting on b.
    return 6


executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)

再举一例：

def wait_on_future():
    f = executor.submit(pow, 5, 2)
    # This will never complete because there is only one worker thread and
    # it is executing this function.
    print(f.result())

executor = ThreadPoolExecutor(max_workers=1)
executor.submit(wait_on_future)


concurrent.futures.ThreadPoolExecutor(max_workers=None, thread_name_prefix='', initializer=None, initargs=())
这个 Executor 子类最多用 max_workers 个线程来异步执行调用。

initializer 是一个可选的可调用对象，会在每个 worker 线程启动之前调用。
initargs 是传递给 initializer 的参数元组。
如果 initializer 抛出了异常，那么当前所有等待的任务都会抛出 BrokenThreadPool 异常，继续提交 submit 任务也会抛出此异常。

3.5 的变化：如果 max_worker 没有指定或者为 None，则默认为本机处理器数量乘以 5。
3.6 新特性：添加了 thread_name_prefix 参数，可以控制由线程池创建的工作线程名称，便于调试。
3.7 的变化：添加了 initializer 和 initargs 参数。

\ProcessPoolExecutor 进程池执行器
ProcessPoolExecutor 进程池执行器类是 Executor 执行器类的子类，使用进程池来异步执行调用。
ProcessPoolExecutor 使用了 multiprocessing 模块，这允许它可以规避 Global Interpreter Lock，但是也意味着只能执行和返回可序列化的（picklable）对象。

__main__ 模块必须被 worker 子进程导入，这意味着 ProcessPoolExecutor 在交互解释器中无法工作。

在已经被提交到 ProcessPoolExecutor 中的可调用对象内使用 Executor 或者 Future 方法会导致死锁。

concurrent.futures.ProcessPoolExecutor(max_workers=None, mp_context=None, initializer=None, initargs=())
这个 Executor 子类最多用 max_workers 个进程来异步执行调用。
如果不指定 max_workers 或者为 None，它默认为本机的处理器数量。
如果 max_workers 小于等于 0，会抛出 ValueError 异常。
mp_context 是多进程上下文（multiprocessing context）或者 None，它会被用来启动 workers。如果不指定 mp_context 或者为 None，会使用默认的多进程上下文环境。

initializer 是一个可选的可调用对象，会在每个 worker 进程启动之前调用。
initargs 是传递给 initializer 的参数元组。
如果 initializer 抛出了异常，那么当前所有等待的任务都会抛出 BrokenProcessPool 异常，继续提交 submit 任务也会抛出此异常。

3.3 版本的变化：任意一个工作进程突然中止时，会抛出 BrokenProcessPool 异常。之前版本中，行为是未定义的，而且对于执行器或者它的 future 对象的操作通常会无响应或者死锁。
3.7 版本的变化：加入了 mp_context 参数，允许用户控制由进程池创建的工作进程的 start_method 方法。该版本还加入了 initializer 和 initargs 参数。




\案例（进程池、线程池）
# 程序的执行方式：
    #一：串行执行
    #二：并行执行

# 提交任务的方式：
    #同步调用(串行执行)：提交一个任务后，在原地等着，等到该任务运行完毕，拿到结果以后，再执行下一行代码
    #异步调用（并行执行）：提交一个任务后，不用在原地等着，直接执行下一行代码，结果呢？

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor,Executor # 前两个继承自Executor,Executor是个抽象类定义了一些规则。子类要遵循。
import time,os,random

def task(i):
    print('%s is running %s' %(os.getpid(),i))
    time.sleep(random.randint(1,3)) # 随机等待秒数
    return i**2 # 返回函数执行结果

if __name__ == '__main__':
    print(os.cpu_count())       # 查看系统cpu个数
    # pool=ProcessPoolExecutor(5)
    pool=ProcessPoolExecutor() # 进程池，进程池大小不写默认以系统cpu个数为准
    # pool=ThreadPoolExecutor() # 线程池，其他的不用动。

    objs=[]
    for i in range(10):
        obj=pool.submit(task,i) # 异步的方式提交任务
        objs.append(obj) # 取到函数执行结果追加到列表，不需要等待依然是并行执行。

        # res=pool.submit(task,i).result() # 同步方式提交任务，使用 result 方法取进程的执行结果。
        # print(res) # 取到函数执行结果，这样需要等待每次的执行结果，就变成串行执行了。效率低没意义。

    pool.shutdown(wait=True) # shutdown代表不允许再往进程池里提交任务,wait=True就是join的意思：等待任务都执行完毕。先关闭进程池禁止提交任务，再等进程池现有的执行完毕。
    print('主')
    for obj in objs:
        print(obj.result())

'''执行时 回车断开
4
4948  is running 0 
8504  is running 1 
8656  is running 2 
7216  is running 3 


8504  is running 4 
8656  is running 5 

8504  is running 6
7216  is running 7

4948  is running 8
8656  is running 9
主
0
1
4
9
16
25
36
49
64
81
'''
