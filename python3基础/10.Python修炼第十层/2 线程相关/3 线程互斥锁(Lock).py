from threading import Thread,Lock
import time

n=50

def task():
    global n
    lock.acquire() # 加锁，确定加锁位置。保证每次都能成功减1。其他线程等着抢锁。
    temp=n
    time.sleep(0.1)
    n=temp-1
    lock.release() # 解锁

if __name__ == '__main__':
    lock=Lock()    # 创建锁,子线程
    t_l=[]
    for i in range(50):
        t=Thread(target=task)
        t_l.append(t)
        t.start()
    for t in t_l:
        t.join()
    print('主',n)  # 主 0
