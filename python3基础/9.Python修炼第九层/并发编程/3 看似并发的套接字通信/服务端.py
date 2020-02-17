from socket import *    # 函数内部不能使用 * 的语法 
from multiprocessing import Process
import time

server=socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.listen(5)  # 最大挂起链接数（比如一起来10个，同时进行的只有5个。并发时这个参数才有意义）

def talk(conn,client_addr):
    while True:
        try:
            msg=conn.recv(1024)
            if not msg:break
            conn.send(msg.upper())
            # time.sleep(10)  # 只是看似是并发，如果程序里不是只回复一个大写，而是需要处理很多数据。用这种方式就看不到并发的效果了。
        except Exception:
            break
    conn.close()

if __name__ == '__main__': 
    while True:
        conn,client_addr=server.accept()
        print('客户端 %s %s' %(client_addr[0],client_addr[1]))
        p=Process(target=talk,args=(conn,client_addr))
        p.start()
    server.close()

# 还可以写成下面的形式
from socket import *    # 函数内部不能使用 * 的语法
from multiprocessing import Process

def talk(conn,client_addr):
    while True:
        try:
            msg=conn.recv(1024)
            if not msg:break
            conn.send(msg.upper())
        except Exception:
            break
    conn.close()

def server():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 8080))
    s.listen(5)  # 最大挂起链接数（比如一起来10个，同时进行的只有5个。并发时这个参数才有意义）
    while True:
        conn,client_addr=s.accept()
        print('客户端 %s %s' %(client_addr[0],client_addr[1]))
        p=Process(target=talk,args=(conn,client_addr))
        p.start()
    s.close()

if __name__ == '__main__':
    server()

# 或者在只样的形式
from socket import *    # 函数内部不能使用 * 的语法
from multiprocessing import Process

s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8080))
s.listen(5)

def talk(conn,client_addr):
    while True:
        try:
            msg=conn.recv(1024)
            if not msg:break
            conn.send(msg.upper())
        except Exception:
            break
    conn.close()

def server():
    while True:
        conn,client_addr=s.accept()
        print('客户端 %s %s' %(client_addr[0],client_addr[1]))
        p=Process(target=talk,args=(conn,client_addr))
        p.start()
    s.close()

if __name__ == '__main__':
    server()

问题
# 因为收到消息后立马回复了一个大写，开启的子进程没有任何耗时。所以上面的方式看起来像是并发，实际是串行执行的。
# 每来一个客户端，都在服务端开启一个进程，如果并发来一个万个客户端，要开启一万个进程吗，你自己尝试着在你自己的机器上开启一万个，10万个进程试一试。
# 解决方法：进程池
