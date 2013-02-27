import util
from view.main_loop import Main_Loop
from model.main_model import Model
from pyplib.client_host import request_exit,send_request
import sys
import os

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print "Client: Starting!"
		pyplib = os.path.join(os.environ['pyp'],'src','share')
		sys.path.insert(0,pyplib)
		util.make_logger()
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
