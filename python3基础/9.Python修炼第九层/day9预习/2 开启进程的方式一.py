from multiprocessing import Process
import time
def work(name):
    print('task <%s> is runing' %name)
    time.sleep(2)
    print('task <%s> is done' % name)

if __name__ == '__main__':
    # Process(target=work,kwargs={'name':'egon'})
    p1=Process(target=work,args=('egon',))
    p2=Process(target=work,args=('alex',))
    p1.start()
    p2.start()
    print('主')