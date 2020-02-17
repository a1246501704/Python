import socket

# ss = socket()  #创建服务器套接字
# ss.bind()      #把地址绑定到套接字
# ss.listen()    #监听链接
# inf_loop:      #服务器无限循环
#     cs = ss.accept() #接受客户端链接
#     comm_loop:       #通讯循环
#         cs.recv()/cs.send() #对话(接收与发送)
#     cs.close()    #关闭客户端套接字
# ss.close()        #关闭服务器套接字(可选)

#买手机（创建服务器套接字）
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # SOCK_STREAM 代表TCP协议

#绑定手机卡（把地址绑定到套接字）
phone.bind(('127.0.0.1',8080))

#开机（监听链接）
phone.listen(5) # 5代表最大挂起的连接数

#等电话链接
print('starting...')
conn,client_addr=phone.accept() #套接字链接,客户端的ip和port（接受客户端链接）
print('=========>')
print(conn)        # <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8080), raddr=('127.0.0.1', 63733)>
print(client_addr) # ('127.0.0.1', 63733)

#收消息
data=conn.recv(1024) # 1024最大的限制，1024 是个坑
print('客户端数据: ',data)

#发消息
conn.send(data.upper())

#挂电话（关闭客户端套接字）
conn.close()

#关机（关闭服务器套接字）
phone.close()

===========================================================================================
#_*_coding:utf-8_*_
__author__ = 'zhanghongyang'

import socket
ip_port=('127.0.0.1',9000)  # 电话卡
BUFSIZE=1024                # 收发消息的尺寸
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
s.bind(ip_port) # 手机插卡
s.listen(5)     # 手机待机

conn,addr=s.accept()            # 手机接电话
# print(conn)
# print(addr)
print('接到来自%s的电话' %addr[0])

msg=conn.recv(BUFSIZE)          # 听消息,听话
print(msg,type(msg))

conn.send(msg.upper())          # 发消息,说话

conn.close()                    # 挂电话

s.close()                       # 手机关机
