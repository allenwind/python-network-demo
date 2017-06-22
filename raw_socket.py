import socket
import os

host = socket.gethostbyname(socket.gethostname())
# host = '172.16.8.1'

if os.name == 'nt':
    protocol = socket.IPPROTO_IP
else:
    protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, protocol)
sniffer.bind((host, 0))

sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

if os.name == 'nt':
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

ips = set()

while True:
    data, address = sniffer.recvfrom(65536)
    if address not in ips:
        print(address)
        ips.add(address)
    #print(data)
        print('\n')

if os.name == 'nt':
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


print(d)
