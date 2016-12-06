import struct
import socket

def ip2int(address):
    return struct.unpack('!I', socket.inet_aton(address))[0]

def int2ip(integer):
    return socket.inet_ntoa(struct.pack('!I', integer))

def test():
    address = '192.168.1.1'
    integer = ip2int(address)
    print(integer)
    address = int2ip(integer)
    print(address)