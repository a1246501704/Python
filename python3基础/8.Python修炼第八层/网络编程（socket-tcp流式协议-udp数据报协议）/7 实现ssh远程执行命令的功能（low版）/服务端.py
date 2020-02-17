import socket
import subprocess
import struct

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM代表TCP协议
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',8080))
phone.listen(5)

while True:
    conn,client_addr=phone.accept() #(套接字链接,客户端的ip和port)
    print(client_addr)

    while True: #通信循环
        #收消息
        try:
            cmd=conn.recv(1024) # 1024最大的限制
            if not cmd:break #针对linux系统

            #执行，拿到执行结果
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)

            stdout_res=obj.stdout.read() # 命令的执行结果
            stderr_res=obj.stderr.read() # 命令的执行结果
            #先发报头
            total_size=len(stderr_res)+len(stdout_res)
            conn.send(struct.pack('i',total_size)) # 将数据总大小打包成了4个butes发送给客户端

            #再发真是的数据
            # conn.send(stdout_res+stderr_res)
            conn.send(stdout_res)
            conn.send(stderr_res)
        except ConnectionResetError:
            break

    #挂电话
    conn.close()

#关机
phone.close()