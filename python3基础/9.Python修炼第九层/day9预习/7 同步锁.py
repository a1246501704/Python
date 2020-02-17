
# Lock锁

# from multiprocessing import Process,Lock
# import time
# def work(name,mutex):
#     mutex.acquire() #加上锁
#     print('task <%s> is runing' %name)
#     time.sleep(2)
#     print('task <%s> is done' % name)
#     mutex.release() #关闭锁
#
# if __name__ == '__main__':
#     mutex=Lock() #定义锁
#     p1=Process(target=work,args=('egon',mutex))
#     p2=Process(target=work,args=('alex',mutex))
#     p1.start()
#     p2.start()
#     print('主')

