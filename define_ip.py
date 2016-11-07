import sys
import re

from random import randint

from scapy.all import IP, TCP, UDP, conf, send

def send_packet(protocol=None, src_ip=None, src_port=None, flags=None, dst_ip=None, dst_port=None, iface=None):
    if protocol == 'tcp':
        packet = IP(src=src_ip, dst=dst_ip)/TCP(flags=flags, sport=src_port, dport=dst_port)
    elif protocol == 'udp':
        if flags:
            raise Exception("flags are not supported for udp")
            packet = IP(src=src_ip, dst=dst_ip)/UDP(sport=src_port, dport=dst_port)
    else:
        raise Exception("Unkonwn protocol %s" % protocol)

    send(packet, iface=iface)

if __name__ == '__main__':
    while True:
        send_packet(protocol='tcp', src_ip='144.168.61.37', src_port=443, flags=1, dst_ip='124.168.61.37', dst_port=8080)