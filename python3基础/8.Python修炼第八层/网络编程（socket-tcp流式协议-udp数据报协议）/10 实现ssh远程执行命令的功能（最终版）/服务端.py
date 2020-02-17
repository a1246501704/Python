import socket
import subprocess
import struct
import json

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # SOCK_STREAM代表TCP协议
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',8080))
phone.listen(5)

while True:
    conn,client_addr=phone.accept() # 链接循环，收到一个元祖(客户端套接字链接,客户端的ip和port)。
    print(client_addr)

    while True: # 通信循环
        #收消息
        try:
            cmd=conn.recv(1024) # 1024最大的限制
            if not cmd:break    # 针对linux系统

            #执行linux命令，拿到执行结果
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)

            stdout_res=obj.stdout.read()
            stderr_res=obj.stderr.read()

            # 解决问题1:struct模块的q模式也无法支持数据无限大
            # 解决问题2:报头不应该仅仅只包含数据大小，如md5加密值、文件名等
            # 制作报头
            header_dic = {
                'filename': 'a.txt',
                'total_size': len(stdout_res)+len(stderr_res), # 数据总大小
                'md5': 'xxxxxxxxx'
            }
            head_json = json.dumps(header_dic) # 序列化
            head_bytes = head_json.encode('utf-8') # 序列化后就是json格式的字符串，然后再encode。

            #先发报头长度
            conn.send(struct.pack('i',len(head_bytes))) # i代表打包后的结果为4个字节，打包的目标是整形数字。

            #再发报头
            conn.send(head_bytes)

            #最后发真实的数据
            # conn.send(stdout_res+stderr_res)
            conn.send(stdout_res)
            conn.send(stderr_res)
        except ConnectionResetError:
            break
    #挂电话
    conn.close()
#关机
phone.close()