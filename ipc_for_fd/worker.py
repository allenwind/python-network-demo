import socket
import struct

def recv_fd(sock):
    msg, ancdata, flags, addr = sock.recvmsg(1,
                                             socket.CMSG_LEN(struct.calcsize('i')))

    cmsg_level, cmsg_type, cmsg_data = ancdata[0]

    assert cmsg_level == socket.SOL_SOCKET and cmsg_type == socket.SCM_RIGHTS
    sock.sendall(b'OK')

    return struct.unpack('i', cmsg_data)[0]

def worker(server_address):
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serv.connect(server_address)
    
    while True:
        fd = recv_fd(serv)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=fd) as client:
            while True:
                msg = client.recv(1024)
                if not msg:
                    break
                print('work: recv {!r}'.format(msg))
                client.send(msg)

    
worker(('', 8080))
