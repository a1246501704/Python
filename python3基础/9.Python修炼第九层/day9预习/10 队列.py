
# 进程彼此之间互相隔离，要实现进程间通信（IPC）
# multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的


from multiprocessing import Queue

# q=Queue(3)
#
# q.put('first')
# q.put('second')
# q.put('third')
# # q.put('fourth')
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())

#了解
q=Queue(3)

q.put('first',block=False)
q.put('second',block=False)
q.put('third',block=False)
# q.put_nowait('fourth') #q.put('fourth',block=False)
q.put('fourth',timeout=3)

