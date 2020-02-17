from socket import *

client=socket(AF_INET,SOCK_DGRAM)
# client.connect(('127.0.0.1',8080)) #udp没有连接

while True:
    msg=input('>>: ').strip()
    client.sendto(msg.encode('utf-8'),('127.0.0.1',8080))

    msg,server_addr=client.recvfrom(1024)
    print(msg.decode('utf-8'))


========================================================================
import socket
ip_port=('127.0.0.1',9000)
BUFSIZE=1024
udp_server_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg=input('>>: ').strip()
    if not msg:continue

    udp_server_client.sendto(msg.encode('utf-8'),ip_port)

    back_msg,addr=udp_server_client.recvfrom(BUFSIZE)
    print(back_msg.decode('utf-8'),addr)