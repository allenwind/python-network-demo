import socket
import struct

def send_fd(sock, fd):
    sock.sendmsg([b'x'],
                 [(socket.SOL_SOCKET, socket.SCM_RIGHTS, struct.pack('i', fd))])

    ack = sock.recv(2)
    assert ack == b'OK'

def server(work_address, port):
    work_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    work_serv.bind(work_address)
    work_serv.listen(1)
    worker, addr = work_serv.accept()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(('', port))
    s.listen(1)

    while True:
        client, addr = s.accept()
        print("server: got connection from", addr)
        send_fd(worker, client.fileno())
        client.close()


server(('', 8000), 8080)     
