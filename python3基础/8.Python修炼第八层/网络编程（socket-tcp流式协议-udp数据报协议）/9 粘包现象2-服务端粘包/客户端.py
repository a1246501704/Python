from socket import *


client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))


client.send('hello'.encode('utf-8')) # 发个5个字节
import time
time.sleep(3)
client.send('world'.encode('utf-8'))