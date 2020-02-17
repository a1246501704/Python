from socket import *


client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))


client.send('hello'.encode('utf-8'))
# import time
# time.sleep(10)    # 时间间隔大的包不会粘在一起，不加sleep这俩个数据包是在客户端粘的
client.send('world'.encode('utf-8'))