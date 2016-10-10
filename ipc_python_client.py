from multiprocessing.connection import Client

c = Client(('localhost', 8080), authkey=b'task')
c.send(object())
c.recv()