from socket import *

server=socket(AF_INET,SOCK_DGRAM) # 数据  udp自带报头
server.bind(('127.0.0.1',8080))

msg1,client_addr=server.recvfrom(100000000) # 客户端发送的数据量如果比这个大，其他的数据就丢了。因为tcp有三次握手、数据传输+确认、四次挥手。udp发完就不管了。udp有效传输是512个bytes
msg2,client_addr=server.recvfrom(1024)
msg3,client_addr=server.recvfrom(1024)

print(msg1)
print(msg2)
print(msg3)
'''
b'hello'
b'world'
b'egon'
'''
# import os
# os.fork
