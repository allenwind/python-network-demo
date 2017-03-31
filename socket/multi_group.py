import socket
import struct
import sys

message = b'very important data'
group = ('224.3.29.71', 10000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(0.2)

ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    while True:
        sent = sock.sendto(message*1000, group)
    while True:
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('timeout')
            break
        else:
            print(data, server)
finally:
    sock.close()
