import socket
import util
from control.command_handler import handle

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
			if 'exit' in resp:
				break

	def listen_for_request(self,model):
		c,addr = self.s.accept()
		util.logger.debug('Established Connection from %s',str(addr))
		request = c.recv(1024)
		util.logger.info('Recieved Request from %s',str(addr))
		ret = handle(request,model)
		util.logger.debug('Handled Request to %s',str(addr))
		c.send(ret)
		util.logger.info('Sent Response to %s',str(addr))
		c.close()
		return ret
