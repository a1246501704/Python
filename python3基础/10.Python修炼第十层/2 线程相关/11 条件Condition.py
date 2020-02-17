# 使得线程等待，只有满足某条件时，才释放n个线程
import threading
 
def run(n):
    con.acquire()
    con.wait()
    print("run the thread: %s" %n)
    con.release()
 
if __name__ == '__main__':
 
    con = threading.Condition()
    for i in range(10):
        t = threading.Thread(target=run, args=(i,))
        t.start()
 
    while True:
        inp = input('>>>')
        if inp == 'q':
            break
        con.acquire()
        con.notify(int(inp))
        con.release()


def condition_func():

    ret = False
    inp = input('>>>')
    if inp == '1':
        ret = True

    return ret


# def run(n):
#     con.acquire()
#     con.wait_for(condition_func)
#     print("run the thread: %s" %n)
#     con.release()

# if __name__ == '__main__':

#     con = threading.Condition()
#     for i in range(10):
#         t = threading.Thread(target=run, args=(i,))
#         t.start()