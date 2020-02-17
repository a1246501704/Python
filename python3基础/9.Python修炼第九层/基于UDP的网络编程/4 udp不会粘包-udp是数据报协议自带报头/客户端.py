from socket import *

client=socket(AF_INET,SOCK_DGRAM) #数据 报协议

client.sendto('hello'.encode('utf-8'),('127.0.0.1',8080))
client.sendto('world'.encode('utf-8'),('127.0.0.1',8080))
client.sendto('egon'.encode('utf-8'),('127.0.0.1',8080))

