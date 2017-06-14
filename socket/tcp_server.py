import os
import random
import socket

# 套接字的半开状态
# socket.SHUT_WD

def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length-len(data))
        if not more:
            raise EOFError("socket closed")
        data += more
    return data

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #立即使用TIME_WAIT状态的socket
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))
    sock.listen(5)
    while True:
        client, socketname = sock.accept()