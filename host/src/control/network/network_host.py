from src.control.game_logic.command_handler import handle

import socket


class Listener:
	def __init__(self):
		self.s = socket.socket()
		self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		host = 'localhost'
		port = 52690
		self.s.bind((host,port))
		self.s.listen(1)

	def listen_for_requests(self,model):
		while True:
			resp = self.listen_for_request(model)
			if 'done' in resp:
				break
		
	def listen_for_request(self,model):
		c,addr = self.s.accept()
		request = c.recv(1024)
		ret = handle(request,model)
		c.send(ret)
		c.close()
		return ret
