from socket import *


server=socket(AF_INET,SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.listen()

conn,addr=server.accept()

data1=conn.recv(1) # 收了一个，剩下的和data2粘在了一起
print('data1:',data1)
import time
time.sleep(5)
data2=conn.recv(1024)
print('data2:',data2)

# 不管是在客户端还是在服务端都会出现粘包的问题，主要原因是因为服务端不知道客户端到底发的数据包有多大。