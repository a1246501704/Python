#!/usr/bin/env python
#_*_coding:utf-8_*_

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):

        while True:
            self.data = self.request.recv(1024).strip()
            print(self.client_address[0])
            print(self.data)
            self.request.sendall(self.data.upper())

if __name__ == '__main__':
    HOST, PORT = "localhost", 9001

    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)


    server.serve_forever()


