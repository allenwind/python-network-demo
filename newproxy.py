import socket
import threading
import queue

def client_proxy(local_address):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(local_address)
    server.listen(5)
    server.settimeout(2)


class ProxyServer:
    def __init__(self, local_address, remote_address, timeout):
        self.local_address = local_address
        self.remote_address = remote_address
        self.timeout = timeout
        self._local_queue = queue.Queue()
        self._remote_queue = queue.Queue()

    def local_proxy(self):
        #a server
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(self.local_address)
        server.listen(5)
        while True:
            sock, address = server.accept()
            self._local_queue.put((sock, address))


    def remote_proxy(self):
        #a client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(self.timeout)
        while True:
            


    def log_system(self):
        pass





