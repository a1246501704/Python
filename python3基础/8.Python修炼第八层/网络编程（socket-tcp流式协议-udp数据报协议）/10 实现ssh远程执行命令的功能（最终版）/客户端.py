import socket
import struct
import json

#买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM代表TCP协议

#发起电话链接
phone.connect(('127.0.0.1',8080))

while True:
    #发消息
    cmd=input('>>: ').strip()
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))

    #先收报头长度
    struct_res=phone.recv(4) # 先收服务端发的报头长度
    header_size=struct.unpack('i',struct_res)[0] # struct解压 取到报头的大小

    #再收报头
    head_bytes=phone.recv(header_size)   # 收报头
    head_json=head_bytes.decode('utf-8') # 编码
    head_dic=json.loads(head_json)       # 序列化
    print(head_dic)

    #最收消息
    cmd_res=b''
    recv_size=0
    total_size=head_dic['total_size'] # 从字典中取到总数据大小
    while recv_size < total_size:
        recv_data=phone.recv(1024) # recv_data是每次收过来真实的大小，即使最后一次收到5个字节。
        cmd_res+=recv_data         # 真实的数据
        recv_size+=len(recv_data)  # 已经收取了多少

    print(cmd_res.decode('utf-8')) # 打印总数据

#关机
phone.close()
