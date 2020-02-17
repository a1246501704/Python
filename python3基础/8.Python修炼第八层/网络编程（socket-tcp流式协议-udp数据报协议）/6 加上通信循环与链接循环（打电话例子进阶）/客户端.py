import socket

#买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM代表TCP协议

#发起电话链接
phone.connect(('127.0.0.1',8080))


while True:
    #发消息
    msg=input('>>: ').strip()
    if not msg:continue
    phone.send(msg.encode('utf-8'))
    print('has send====>')
    #收消息
    data=phone.recv(1024)
    print('has recv=====>')
    print(data.decode('utf-8'))

#关机
phone.close()

============================================================================================客户端改进版

#_*_coding:utf-8_*_
__author__ = 'zhanghongyang'
import socket
ip_port=('127.0.0.1',8081)
BUFSIZE=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect_ex(ip_port)              #拨电话

while True:                        #新增通信循环,客户端可以不断发收消息
    msg=input('>>: ').strip()
    if len(msg) == 0:continue
    s.send(msg.encode('utf-8'))    #发消息,说话(只能发送字节类型)

    feedback=s.recv(BUFSIZE)       #收消息,听话
    print(feedback.decode('utf-8'))

s.close()                          #挂电话










