import ssl
import os

from socket import socket, AF_INET, SOCK_STREAM
from xmlrpc.client import ServerProxy

"""
s = socket(AF_INET, SOCK_STREAM)
s_ssl = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='ssl_cert.pem')
s_ssl.connect(('localhost', 8080))
s_ssl.send(b'are you recv?')
s_ssl.recv(1024)"""

s = ServerProxy('https://localhost:8080', allow_none=True)
