import util
from view.main_loop import Main_Loop
from model.main_model import Model
from pyplib.client_host import request_exit,send_request
import sys

if __name__ == '__main__':
	if len(sys.argv) == 1:
		util.make_logger()
		util.logger.info('Started Client')
		model = Model()
		main = Main_Loop(model)
		main.run()
	else:
		if sys.argv[1] == 'b':
			request = '<request'
			print send_request(request)
		elif sys.argv[1] == 'd':
			print request_exit(0)
