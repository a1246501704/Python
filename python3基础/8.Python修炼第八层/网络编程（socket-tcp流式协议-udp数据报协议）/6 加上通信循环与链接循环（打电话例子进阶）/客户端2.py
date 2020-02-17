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











