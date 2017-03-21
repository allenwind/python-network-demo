import time
import socket
import select

"""
利用Python的一个IO复用例子，使用epoll模型
"""

default = True

if default:
    EOL1 = b'\n\n'
    EOL2 = b'\n\r\n'
    response  = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 2017 01:01:01 GMT\r\n'
    response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
    response += b'Hello, world!'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) #TCP_NODELAY
server.bind(('', 8080))
server.listen(1)
server.setblocking(0)

epoll = select.epoll()
epoll.register(server.fileno(), select.EPOLLIN) #select.EPOLLIN | select.EPOLLET

try:
    connections = {} #{fd: sock}
    requests = {} #{fd: requests}
    responses = {} #{fd: resposne}

    while True:
        events = epoll.poll(timeout=10) #[(fd, event), ...]
        for fileno, event in events:
            if fileno == server.fileno():
                connection, address = server.accept()
                connection.setblocking(0)

                epoll.register(connection.fileno(), select.EPOLLIN)
                connections[connection.fileno()] = connection
                requests[connection.fileno()] = b''
                responses[connection.fileno()] = response

            elif event & select.POLLIN:
                requests[fileno] += connections[fileno].recv(1024)
                if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                    epoll.modify(fileno, select.EPOLLOUT) #修改监听文件描述符的方式，修改文件描述符的事件
                    print('-'*40, requests[fileno].decode()[:-2], sep='\n')

            elif event & select.EPOLLOUT:
                byteswritten = connections[fileno].send(responses[fileno])
                responses[fileno] = responses[fileno][byteswritten:]

                if len(responses[fileno]) == 0:
                    epoll.modify(fileno, 0) #
                    connections[fileno].shutdown(socket.SHUT_RDWR)

            elif event & select.EPOLLHUP:
            #Hang up happened on the assoc. fd
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]

finally:
    epoll.unregister(server.fileno())
    epoll.close()
    server.close()

