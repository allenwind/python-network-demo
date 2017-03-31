import struct
import socket

group = '224.3.29.71'
server_address = ('', 80)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

group = socket.inet_aton(group)
req = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, req)

while True:
    print('wait')
    data, address = sock.recvfrom(1024)
    print(data, address)

    sock.sendto(b'ack', address)
