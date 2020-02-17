from socket import *

server=socket(AF_INET,SOCK_DGRAM) # SOCK_DGRAM是udp协议
server.bind(('127.0.0.1',8080))

# server.listen(5) #udp没有
# server.accept()  #udp没有

# while True:      #udp没有连接，更不可能有连接循环了
    # server.accept() #udp没有

while True: #通信循环
    msg,client_addr=server.recvfrom(1024)
    print(msg)
    server.sendto(msg.upper(),client_addr)


========================================================================
import socket
ip_port=('127.0.0.1',9000)
BUFSIZE=1024
udp_server_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_server_client.bind(ip_port)

while True:
    msg,addr=udp_server_client.recvfrom(BUFSIZE)
    print(msg,addr)

    udp_server_client.sendto(msg.upper(),addr)
