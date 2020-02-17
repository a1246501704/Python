from socket import *

udp_client=socket(AF_INET,SOCK_DGRAM)


udp_client.sendto('hello'.encode('utf-8'),('127.0.0.1',8080))
udp_client.sendto('world'.encode('utf-8'),('127.0.0.1',8080))
