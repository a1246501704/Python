from multiprocessing import Process
import time,os
def work():
    print('parent:%s task <%s> is runing' %(os.getppid(),os.getpid()))
    time.sleep(1000)
    print('parent:%s task <%s> is done'  %(os.getppid(),os.getpid()))


if __name__ == '__main__':
    p1=Process(target=work)
    p1.start()

    # p1.terminate()
    # time.sleep(3)
    # print(p1.is_alive())
    # print(p1.name)
    # print(p1.pid)
    print('主',os.getpid(),os.getppid())
    time.sleep(10000)