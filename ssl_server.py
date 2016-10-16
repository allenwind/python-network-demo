import ssl
import os

from socket import socket, AF_INET, SOCK_STREAM
from xmlrpc.server import *

KEYFILE = 'ssl_key.pem'
CERTFILE = 'ssl_cert.pem'

def echo_client(s):
    while True:
        data = s.recv(8192)
        if data == b'':
            break
        s.send(data)
    s.close()
    print('Connection closed')

def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)

    s_ssl = ssl.wrap_socket(s, 
                            keyfile=KEYFILE,
                            certfile=CERTFILE,
                            server_side=True)
    while True:
        try:
            client, addr = s_ssl.accept()
            print('Got connection', client, addr)
            echo_client(client)
        except Exception as error:
            print('{}: {}'.format(error.__class__.__name__, error))

class SSLMixin:
    def __init__(self, *args, keyfile=None, certfile=None, ca_certs=None,
                 cert_reqs=ssl.CERT_REQUIRED, **kwargs):
        self._keyfile = keyfile
        self._certfile = certfile
        self._ca_certs = ca_certs
        self._cert_reqs = cert_reqs
        super().__init__(*args, **kwargs)

    def get_request(self):
        client, addr = super().get_request()
        client_ssl = ssl.wrap_socket(client, 
                                     keyfile=self._keyfile,
                                     certfile=self._certfile,
                                     ca_certs=self._ca_certs,
                                     cert_reqs=self._cert_reqs,
                                     server_side=True)
        return client_ssl, addr

class SSLSimpleXMLRPCServer(SSLMixin, SimpleXMLRPCServer):
    pass

class KeyValueServer:
    _rpc_methods = ['get', 'set', 'delete', 'exists', 'keys']
    def __init__(self, *args, **kwargs):
        self._data = {}
        self._serv = SSLSimpleXMLRPCServer(*args, allow_none=True, **kwargs)
        for name in self._rpc_methods:
            self._serv.register_function(getattr(self, name))

    def get(self, name):
        return self._data[name]

    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        del self._data[name]

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def serve_forever(self):
        self._serv.serve_forever()

if __name__ == '__main__':
    path = 'E:\\github\\net'
    os.chdir(path)



    kvserver = KeyValueServer(('localhost', 8080),
                              keyfile=KEYFILE,
                              certfile=CERTFILE)
    kvserver.serve_forever()




