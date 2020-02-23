# queue队列 ：使用import queue，用法与进程Queue一样


\class queue.Queue(maxsize=0) # 队列(吃完拉)，先进先出
import queue

q=queue.Queue()
q.put('first')
q.put('second')
q.put('third')

print(q.get())
print(q.get())
print(q.get())
'''
结果(先进先出):
first
second
third
'''

\class queue.LifoQueue(maxsize=0) # 堆栈(吃完吐)，后进先出。last in fisrt out，
import queue

q=queue.LifoQueue()
q.put('1')
q.put('2')
q.put('3')

print(q.get())
print(q.get())
print(q.get())
'''
结果(后进先出):
3
2
1
'''

\class queue.PriorityQueue(maxsize=0) # 优先级的队列。以元祖的形式存储。
import queue

q=queue.PriorityQueue()
#put进入一个元组,元组的第一个元素是优先级(通常是数字,也可以是非数字之间的比较),数字越小优先级越高
q.put((20,'a'))
q.put((10,'b'))
q.put((30,'c'))
q.put((-1,'d'))

print(q.get())
print(q.get())
print(q.get())
'''
结果(数字越小优先级越高,优先级高的优先出队):
(-1, 'd')
(10, 'b')
(20, 'a')
(30, 'c')
'''
