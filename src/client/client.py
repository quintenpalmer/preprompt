import socket
import sys
import os

pyplib = os.path.join(os.environ['pyp'],'src','share','py')
sys.path.insert(0,pyplib)
from pyplib import util
from pyplib.client_host import request_exit,send_request,request_test

from model.main_model import Model
from view.main_loop import Main_Loop

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print "Client: Starting!"
		util.make_logger('client')
		util.logger.info('Started Client')
		model = Model(uid=1)
		main = Main_Loop(model)
		main.run()
		print "Client: Exiting!"
	else:
		if sys.argv[1] == 'b':
			request = '<request'
			send_request(request)
			print "Client: Sent bad data!"
		elif sys.argv[1] == 'd':
			request_exit(0)
			print "Client: Sent shutdown to server!"
		elif sys.argv[1] == 'c':
			try:
				request_test(0)
				print "Server is UP!"
			except socket.error:
				print "Server is DOWN!"
