import hmac
from socket import socket, AF_INET, SOCK_STREAM


def client_authenticate(connection, secret_key):
	message = connection.recv(320)
	hash_ = hmac.new(secret_key, message)
	digest = hash_.digest()
	connection.send(digest)

def main(secret_key=b'task'):
	
	s = socket(AF_INET, SOCK_STREAM)
	s.connect(('localhost', 8080))
	client_authenticate(s, secret_key)
	s.send(b'OK')
	response = s.recv(1024)
	return response

if __name__ == '__main__':
	main()
