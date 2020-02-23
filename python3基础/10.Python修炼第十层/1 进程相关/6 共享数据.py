# 进程间通信应该尽量避免使用本节所讲的共享数据的方式

# 进程间数据是独立的，可以借助于队列或管道实现通信，二者都是基于消息传递的。
# 虽然进程间数据独立，但可以通过Manager实现数据共享，事实上Manager的功能远不止于此。

from multiprocessing import Process,Manager,Lock # manager就能创建出来一块共享内存，可以放列表、字典等python数据类型。
import time

def task(d,lock):
    with lock: # 不加锁而操作共享的数据,肯定会出现数据错乱
        time.sleep(1)
        d['count'] -= 1

if __name__ == '__main__':
    lock=Lock()
    m=Manager()
    d=m.dict({"count":10})
    p_l=[]
    for i in range(10):
        p=Process(target=task,args=(d,lock))
        p_l.append(p)
        p.start()

    for p in p_l:
        p.join()

    print(d)