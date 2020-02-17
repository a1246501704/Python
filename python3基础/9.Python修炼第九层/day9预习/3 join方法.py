from multiprocessing import Process
import time
def work(name):
    print('task <%s> is runing' %name)
    time.sleep(3)
    print('task <%s> is done' % name)

if __name__ == '__main__':
    p1=Process(target=work,args=('egon',))
    p2=Process(target=work,args=('alex',))
    p3=Process(target=work,args=('yuanhao',))

    # p1.start()
    # p2.start()
    # p3.start()
    #
    # p1.join() #主进程等，等待p1运行结束
    # p2.join() #主进程等，等待p2运行结束
    # p3.join() #主进程等，等待p3运行结束

    p_l = [p1, p2, p3]
    for p in p_l:
        p.start()

    for p in p_l:
        p.join()

    print('主')

    # p_l = [p1, p2, p3]
    # for p in p_l:
    #     p.start()
    #     p.join()
    # p1.start()
    # p1.join()
    # p2.start()
    # p2.join()
    # p3.start()
    # p3.join()


    # print('主')
