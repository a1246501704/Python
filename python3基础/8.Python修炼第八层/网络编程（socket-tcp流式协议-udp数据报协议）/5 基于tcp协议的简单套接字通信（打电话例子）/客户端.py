import socket

# cs = socket()    # 创建客户套接字
# cs.connect()     # 尝试连接服务器
# comm_loop:       # 通讯循环
#      cs.send()/cs.recv()    # 对话(发送/接收)
# cs.close()       # 关闭客户套接字


#买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM代表TCP协议

#发起电话链接
phone.connect(('127.0.0.1',8080)) # 对应服务端的accept

#发消息
phone.send('hello'.encode('utf-8'))

#收消息
data=phone.recv(1024) 
print(data)

#关机
phone.close()

============================================================================================
#_*_coding:utf-8_*_
__author__ = 'zhanghongyang'
import socket
ip_port=('127.0.0.1',9000)
BUFSIZE=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect_ex(ip_port)    # 拨电话

s.send('zhanghongyang nb'.encode('utf-8')) # 发消息,说话(只能发送字节类型)

feedback=s.recv(BUFSIZE)                   # 收消息,听话
print(feedback.decode('utf-8'))

s.close()                                  # 挂电话
