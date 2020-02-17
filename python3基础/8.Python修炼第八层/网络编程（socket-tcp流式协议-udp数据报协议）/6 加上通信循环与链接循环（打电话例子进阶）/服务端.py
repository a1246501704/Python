import socket

#买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM代表TCP协议
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) # 解决地址端口被占用，在bind前加入一条socket配置，重用ip和端口

#绑定手机卡
phone.bind(('127.0.0.1',8080))

#开机
phone.listen(5)

#等电话链接
print('starting...')
while True:
    conn,client_addr=phone.accept() #(套接字链接,客户端的ip和port)
    print(client_addr)

    while True: #通信循环
        #收消息
        try:
            data=conn.recv(1024) # 1024最大的限制
            print('客户端数据: ',data)
            if not data:break    # 针对linux系统
            #发消息
            conn.send(data.upper())
        except ConnectionResetError: # 客户端挂断处理
            break

    #挂电话
    conn.close()

#关机
phone.close()

'''解决地址端口被占用  方法二
发现系统存在大量TIME_WAIT状态的连接，通过调整linux内核参数解决，
vi /etc/sysctl.conf

编辑文件，加入以下内容：
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_fin_timeout = 30
然后执行 /sbin/sysctl -p 让参数生效。
net.ipv4.tcp_syncookies = 1  # 表示开启SYN Cookies。当出现SYN等待队列溢出时，启用cookies来处理，可防范少量SYN攻击，默认为0，表示关闭；
net.ipv4.tcp_tw_reuse = 1    # 表示开启重用。允许将TIME-WAIT sockets重新用于新的TCP连接，默认为0，表示关闭；
net.ipv4.tcp_tw_recycle = 1  # 表示开启TCP连接中TIME-WAIT sockets的快速回收，默认为0，表示关闭。
net.ipv4.tcp_fin_timeout     # 修改系統默认的 TIMEOUT 时间
'''


============================================================================================服务端改进版
#_*_coding:utf-8_*_
__author__ = 'zhanghongyang'
import socket
ip_port=('127.0.0.1',8081)#电话卡
BUFSIZE=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
s.bind(ip_port) #手机插卡
s.listen(5)     #手机待机

while True:                         #新增接收链接循环,可以不停的接电话
    conn,addr=s.accept()            #手机接电话
    # print(conn)
    print(addr)
    print('接到来自%s的电话' %addr[0])
    while True:                     #新增通信循环,可以不断的通信,收发消息
        msg=conn.recv(BUFSIZE)      #听消息,听话
        if len(msg) == 0:break      #如果不加,那么正在链接的客户端突然断开,recv便不再阻塞,死循环发生
        print(msg,type(msg))
        conn.send(msg.upper())  #发消息,说话
    conn.close()                #挂电话
s.close()                       #手机关机

