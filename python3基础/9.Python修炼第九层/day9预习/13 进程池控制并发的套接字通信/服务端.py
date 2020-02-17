from multiprocessing import Pool
import os
from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8080))
s.listen(5)
def talK(conn,addr):
    print(os.getpid())
    while True:
        try:
            data=conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except Exception:
            break
    conn.close()

if __name__ == '__main__':
    p=Pool(4)
    while True:
        conn,addr=s.accept()
        p.apply_async(talK,args=(conn,addr))
    s.close()