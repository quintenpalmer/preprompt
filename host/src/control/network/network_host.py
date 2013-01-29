
import socket


class Listener:
	def __init__(self):
		self.s = socket.socket()
		self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		host = 'localhost'
		port = 52690
		self.s.bind((host,port))
		self.s.listen(1)

	def listen_for_requests(self):
		while True:
			request = self.listen_for_request()
			print request
			if request == 'exit':
				break
		
	def listen_for_request(self):
		c,addr = self.s.accept()
		ret = c.recv(1024)
		c.send('hi')
		c.close()
		return ret
