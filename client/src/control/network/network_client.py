
import socket

class Requester:
	def send_request(self,request):
		self.s = socket.socket()
		host = 'localhost'
		port = 52690
		self.s.connect((host,port))

		self.s.send(request)
		response = self.s.recv(1024)
		self.s.close()
		return response

