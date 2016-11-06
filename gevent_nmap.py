import gevent
import socket
import functools
import time
import logging

from gevent import monkey

monkey.patch_socket()

logging.basicConfig(filename=r'd:\logging\nmap.txt', 
                    level=logging.INFO, 
                    format=logging.BASIC_FORMAT)



def timethis(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        logging.info('elapsed time is {}'.format(elapsed))
    return wrapper

def get_port(IP, PORT):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    global port_cell
    try:
        client.connect((IP, PORT))
    except Exception:
        pass
    else:
        port_cell.append(PORT)
    finally:
        client.close()

@timethis
def asynchronous():
    lets = []
    count = 0
    for port in range(1, 65536):
        lets.append(gevent.spawn(get_port, IP, port))
        count = count + 1
        if count == 1000:
            gevent.joinall(lets)
            count = 0
            lets = []
            print(port, port_cell,sep='-->', end='\n')
    gevent.joinall(lets)

if __name__ == '__main__':
    port_cell = []
    IP = '210.38.139.58'
    asynchronous()













        
