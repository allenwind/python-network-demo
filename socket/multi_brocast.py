import socket
import struct

def multi_brocast(group, message, timeout):
    brocaster = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    brocaster.settimeout(timeout)
    ttl = struct.pack('b', 5)
    #socket.setsockopt(level, optname, value) 
    brocaster.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    try:
        while True:
            brocaster.sendto(message, group)
        print('sendto')
        while True:
            data, server = brocaster.recvfrom(100)
    except socket.timeout:
        print('timeout')
    else:
        print(data, server)
    finally:
        brocaster.close()

if __name__ == '__main__':

    group = ('224.3.29.71', 80)
    timeout = 1
    message = b'you are great!'*1000
    multi_brocast(group, message, timeout)

#brocaster = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#brocaster.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
