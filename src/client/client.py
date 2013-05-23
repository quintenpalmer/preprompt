import socket
import sys
import os

from pplib.client_host_json import *

from model import Model
from main_loop import Main_Loop

from drawer import draw

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print "Client: Starting!"
		model = Model(uid=1)
		main = Main_Loop(model)
		main.run()
		print "Client: Exiting!"
	else:
		if sys.argv[1] == 'close':
			print request_exit(0)
			print "Client: Sent shutdown to server!"
		elif sys.argv[1] == 'check':
			try:
				print request_test(0)
				print "Server is UP!"
			except socket.error:
				print "Server is DOWN!"
		elif sys.argv[1] == '-c':
			with open(os.path.join(os.environ['postpromptroot'],'var','log','test.log'),'a') as f:
				main = Main_Loop(Model(uid=1))
				for command in sys.argv[2].split(' '):
					main.run_command(command)
					f.write('%s\n'%main.resp)
					f.write('%s\n'%draw(main.model,main.current_message))
					print draw(main.model,main.current_message)
