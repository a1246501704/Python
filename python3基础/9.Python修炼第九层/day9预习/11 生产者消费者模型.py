# from multiprocessing import Process,Queue
# import time,os
# def producer(q,name):
#     for i in range(3):
#         time.sleep(1)
#         res='%s%s' %(name,i)
#         q.put(res)
#         print('\033[45m<%s> 生产了 [%s]\033[0m' %(os.getpid(),res))
#
#
# def consumer(q):
#     while True:
#         res=q.get()
#         if res is None:break
#         time.sleep(1.5)
#         print('\033[34m<%s> 吃了 [%s]\033[0m' % (os.getpid(), res))
#
# if __name__ == '__main__':
#     q=Queue()
#     #生产者们：即厨师们
#     p1=Process(target=producer,args=(q,'包子'))
#     p2=Process(target=producer,args=(q,'饺子'))
#     p3=Process(target=producer,args=(q,'馄饨'))
#
#     #消费者们：即吃货们
#     c1=Process(target=consumer,args=(q,))
#     c2=Process(target=consumer,args=(q,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     c1.start()
#     c2.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     q.put(None)
#     q.put(None)
#
#     print('主')




# from multiprocessing import Process, JoinableQueue
# import time, os
#
#
# def producer(q, name):
#     for i in range(3):
#         time.sleep(1)
#         res = '%s%s' % (name, i)
#         q.put(res)
#         print('\033[45m<%s> 生产了 [%s]\033[0m' % (os.getpid(), res))
#     q.join()
#
# def consumer(q):
#     while True:
#         res = q.get()
#         time.sleep(1.5)
#         print('\033[34m<%s> 吃了 [%s]\033[0m' % (os.getpid(), res))
#         q.task_done()
#
# if __name__ == '__main__':
#     q = JoinableQueue()
#
#     # 生产者们：即厨师们
#     p1 = Process(target=producer, args=(q, '包子'))
#     p2 = Process(target=producer, args=(q, '饺子'))
#     p3 = Process(target=producer, args=(q, '馄饨'))
#
#     # 消费者们：即吃货们
#     c1 = Process(target=consumer, args=(q,))
#     c2 = Process(target=consumer, args=(q,))
#
#     c1.daemon=True
#     c2.daemon=True
#     p1.start()
#     p2.start()
#     p3.start()
#     c1.start()
#     c2.start()
#
#
#     p1.join()
#
#     print('主')


# -----------------


# from multiprocessing import Process,Queue
# import time
# import os
#
# def producer(q,name):
#     for i in range(3):
#         time.sleep(1)
#         res='%s%s' %(name,i)
#         q.put(res)
#         print('\033[45m<%s> 生产了 [%s]\033[0m' %(os.getpid(),res))
#
#
# def consumer(q):
#     while True:
#         res=q.get()
#         if res is None:break
#         time.sleep(1.5)
#         print('\033[34m<%s> 吃了 [%s]\033[0m' % (os.getpid(), res))
#
# if __name__ == '__main__':
#     q=Queue()
#     #生产者们：即厨师们
#     p1=Process(target=producer,args=(q,'包子'))
#     p2=Process(target=producer,args=(q,'饺子'))
#     p3=Process(target=producer,args=(q,'馄饨'))
#
#     #消费者们：即吃货们
#     c1=Process(target=consumer,args=(q,))
#     c2=Process(target=consumer,args=(q,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     c1.start()
#     c2.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     q.put(None)
#     q.put(None)
#
#     print('主')
#




from multiprocessing import Process,JoinableQueue
import time
import os

def producer(q,name):
    for i in range(3):
        time.sleep(1)
        res='%s%s' %(name,i)
        q.put(res)
        print('\033[45m<%s> 生产了 [%s]\033[0m' %(os.getpid(),res))
    q.join()

def consumer(q):
    while True:
        res=q.get()
        time.sleep(1.5)
        print('\033[34m<%s> 吃了 [%s]\033[0m' % (os.getpid(), res))
        q.task_done()

if __name__ == '__main__':
    q=JoinableQueue()
    #生产者们：即厨师们
    p1=Process(target=producer,args=(q,'包子'))
    p2=Process(target=producer,args=(q,'饺子'))
    p3=Process(target=producer,args=(q,'馄饨'))

    #消费者们：即吃货们
    c1=Process(target=consumer,args=(q,))
    c2=Process(target=consumer,args=(q,))

    c1.daemon=True
    c2.daemon=True

    p1.start()
    p2.start()
    p3.start()

    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
    print('主')


















