# /usr/local/bin/python3
# -*- encoding: utf-8 -*-

import socket

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 8080))
sock.listen(5)

while True:
    conn, addr = sock.accept()  # hang住
    # 有人来连接了
    # 获取用户发送的数据
    data = conn.recv(8096)
    print(conn)
    print(data)
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b'123123')
    conn.close()


