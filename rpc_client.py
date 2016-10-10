from xmlrpc.client import ServerProxy

s = ServerProxy('http://localhost:8080', allow_none=True)
s.set
s.get
s.delete
#...