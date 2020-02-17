from socket import *

server=socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.listen()

conn,addr=server.accept()

data1=conn.recv(5)   # 客户端收的字节小也粘不到一起，比如是收6个就会出现粘包现象。
print('data1:',data1)
data2=conn.recv(5)
print('data2:',data2)


