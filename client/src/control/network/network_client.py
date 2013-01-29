
import socket
host = 'localhost'
port = 52690

def send_request(request):
	s = socket.socket()
	s.connect((host,port))

	s.send(request)
	response = s.recv(1024)
	s.close()
	return response

