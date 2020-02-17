

from multiprocessing import Pool
import os,time

def work(n):
    print('task <%s> is runing' %os.getpid())
    time.sleep(2)
    return n**2
if __name__ == '__main__':
    # print(os.cpu_count())
    p=Pool(4)
    # for i in range(10):
    #     res=p.apply(work,args=(i,))
    #     print(res)

    res_l=[]
    for i in range(10):
        res=p.apply_async(work,args=(i,))
        res_l.append(res)

    p.close()
    p.join()
    #
    # for res in res_l:
    #     print(res.get())



