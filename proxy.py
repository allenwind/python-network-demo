import threading
import socket
import socketserver
import queue

class ProxyHandler(socketserver.StreamRequestHandler):
    disable_nagle_algorithm = True
    
    def setup(self):
        self.remote_address = self.server.remote_address
        self.connection = self.request
        if self.timeout is not None:
            self.connection.settimeout(self.timeout)
        if self.disable_nagle_algorithm:
            self.connection.setsockopt(socket.IPPROTO_TCP,
                                       socket.TCP_NODELAY, True)
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        

    def handle(self):
        self.client.connect(self.remote_address)
        

    def finish(self):
        pass

class ProxyServer(socketserver.ThreadingTCPServer):
    def __init__(self, server_address, RequestHandlerClass, remote_address, bind_and_activate=True):
        socketserver.ThreadingTCPServer.__init__(self, server_address, RequestHandlerClass, bind_and_activate)
        self.remote_address = remote_address
        

    
    
    
