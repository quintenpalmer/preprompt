
import socket
from src import util
host = 'localhost'
port = 52690

def send_request(request):
	s = socket.socket()
	s.connect((host,port))

	s.send(request)
	util.logger.info('Sent request')
	response = s.recv(16384)
	util.logger.info('Received response')
	s.close()
	return response

