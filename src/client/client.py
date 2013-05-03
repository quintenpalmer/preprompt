import socket
import sys
import os

pplib = os.path.join(os.environ['postprompt'],'src','share','py')
sys.path.insert(0,pplib)

from pplib import util
from pplib.client_host import request_exit,send_request,request_test

from model.main_model import Model
from view.main_loop import Main_Loop

from view.drawer import draw

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
		if sys.argv[1] == 'bad':
			request = '<request'
			send_request(request)
			print "Client: Sent bad data!"
		elif sys.argv[1] == 'close':
			print request_exit(0)
			print "Client: Sent shutdown to server!"
		elif sys.argv[1] == 'check':
			try:
				print request_test(0)
				print "Server is UP!"
			except socket.error:
				print "Server is DOWN!"
		elif sys.argv[1] == '-c':
			with open('test.log','a') as f:
				main = Main_Loop(Model(uid=1))
				for command in sys.argv[2].split(' '):
					main.run_command(command)
					f.write('%s\n'%main.resp)
					f.write('%s\n'%draw(main.model,main.current_message))
					print draw(main.model,main.current_message)
				print draw(main.model,main.current_message)
