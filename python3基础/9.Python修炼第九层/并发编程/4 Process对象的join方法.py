from multiprocessing import Process
import time,random

def piao(name):
    print('%s is piaoing' %name)
    time.sleep(random.randint(1,3))
    print('%s is over' % name)


if __name__ == '__main__':
    p1=Process(target=piao,args=('alex1',))
    p1.start()
    print('主') # 如果想让子进程执行完再执行主进程的这行代码，怎么办？使用join方法
'''
主
alex1 is piaoing
alex1 is over
'''

\join方法
from multiprocessing import Process
import time,random

def piao(name):
    print('%s is piaoing' %name)
    time.sleep(random.randint(1,3))
    print('%s is over' % name)


if __name__ == '__main__':
    p1=Process(target=piao,args=('alex1',))
    p1.start()
    p1.join()   # 等待p1执行完才会执行下面主进程的print，join不可以加在start之前。
    print('主')
'''
alex1 is piaoing
alex1 is over
主
'''

\开启多个子进程时join方法的使用场景
from multiprocessing import Process
import time,random

def piao(name):
    print('%s is piaoing' %name)
    time.sleep(random.randint(1,3))
    print('%s is over' % name)


if __name__ == '__main__':
    p1=Process(target=piao,args=('alex1',))
    p2=Process(target=piao,args=('alex2',))
    p3=Process(target=piao,args=('alex3',))

    #串行执行
    # p1.start()
    # p1.join()   # p1执行完了才能执行后面的代码
    # p2.start()
    # p2.join()
    # p3.start()
    # p3.join()

    #并发执行
    # p1.start()  # 发送这三个start信号只是瞬间的事
    # p2.start()
    # p3.start()
    # p3.join()   # 如果p3执行需一个小时、p1执行需30分钟、p2执行需10分钟，当p3执行到10分钟时p2已经执行完了，当p3执行到30分钟时p1已经执行完了。所以主进程一共要等一个小时。
    # p1.join()
    # p2.join()

    #简单写法
    p_l=[p1,p2,p3]
    for p in p_l:
        p.start()
        # p.join()
    for p in p_l:
        p.join()

    print('主')

# join 会让主进程 等待join的子进程结束 才执行主进程的代码


\join：主进程等，等待子进程结束
from multiprocessing import Process
import time
import random

class Piao(Process):
    def __init__(self,name):
        self.name=name
        super().__init__()
    def run(self):
        print('%s is piaoing' %self.name)
        time.sleep(random.randrange(1,3))
        print('%s is piao end' %self.name)


p=Piao('egon')
p.start()
p.join(0.0001) #等待p停止,等0.0001秒就不再等了
print('开始')


\有了join，程序不就是串行了吗？？？
from multiprocessing import Process
import time
import random
def piao(name):
    print('%s is piaoing' %name)
    time.sleep(random.randint(1,3))
    print('%s is piao end' %name)

p1=Process(target=piao,args=('egon',))
p2=Process(target=piao,args=('alex',))
p3=Process(target=piao,args=('yuanhao',))
p4=Process(target=piao,args=('wupeiqi',))

p1.start()
p2.start()
p3.start()
p4.start()

#有的同学会有疑问:既然join是等待进程结束,那么我像下面这样写,进程不就又变成串行的了吗?
#当然不是了,必须明确：p.join()是让谁等？
#很明显p.join()是让主线程等待p的结束，卡住的是主线程而绝非进程p，

#详细解析如下：
#进程只要start就会在开始运行了,所以p1-p4.start()时,系统中已经有四个并发的进程了
#而我们p1.join()是在等p1结束,没错p1只要不结束主线程就会一直卡在原地,这也是问题的关键
#join是让主线程等,而p1-p4仍然是并发执行的,p1.join的时候,其余p2,p3,p4仍然在运行,等#p1.join结束,可能p2,p3,p4早已经结束了,这样p2.join,p3.join.p4.join直接通过检测，无需等待
# 所以4个join花费的总时间仍然是耗费时间最长的那个进程运行的时间
p1.join()
p2.join()
p3.join()
p4.join()

print('主线程')


#上述启动进程与join进程可以简写为
# p_l=[p1,p2,p3,p4]
# 
# for p in p_l:
#     p.start()
# 
# for p in p_l:
#     p.join()



