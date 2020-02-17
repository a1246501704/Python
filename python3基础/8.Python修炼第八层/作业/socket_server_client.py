#!/usr/bin/env python
#_*_coding:utf-8_*_


# import socketserver
import socket
import os
import json


client = socket.socket()
client.connect(('localhost',9001))

while True:
    choice = input(">>").strip()
    if len(choice) == 0:continue
    client.send(choice.encode())
    recv = client.recv(1024)

    print("received:",recv.decode())

