from xmlrpc.server import SimpleXMLRPCServer

#扩展成邮件服务器和其他命令式功能
#手机关掉电脑  -->添加windows守护进程的方式

class KeyValueServer:
    _rpc_methods_ = ['get', 'set', 'delete', 'exists', 'keys']

    def __init__(self, address):
        self._data = {}
        self._serv = SimpleXMLRPCServer(address, allow_none=True)
        for name in self._rpc_methods_:
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

def task():
    pass

if __name__ == '__main__':

    kvserv = KeyValueServer(('', 8080))
    kvserv.register_function(task) #also useful

    kvserv.serve_forever()