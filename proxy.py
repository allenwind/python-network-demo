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
        self.client.connect(self.remote_address)
        
    def handle(self):
        while True:
            try:
                data = self.recv(self.connection, 8192)
            except socket.timeout as error:
                pass

            try:
                self.send(self.client, data)
            except Exception as error:
                pass

            try:
                data = self.recv(self.client, 8192)
                self.send(self.connection, data)
            except Exception as error:
                pass
                
    def finish(self):
        pass

    def send(self, connection, data):
        connection.send(data)

    def recv(self, connection, buffersize):
        buffer = b''
        connection.settimeout(2)
        try:
            while True:
                data = connection.recv(buffersize)
                if not data:
                    break
                buffer += data
        except Exception as error:
            pass
        return buffer


class ProxyServer(socketserver.ThreadingTCPServer):
    def __init__(self, server_address, RequestHandlerClass, remote_address, bind_and_activate=True):
        socketserver.ThreadingTCPServer.__init__(self, server_address, RequestHandlerClass, bind_and_activate)
        self.remote_address = remote_address
        

    

if __name__ == '__main__':
    server_address = ('localhost', 2020)
    remote_address = ('localhost', 8080)

    server = ProxyServer(server_address, ProxyHandler, remote_address)
    server.serve_forever()






    
    
