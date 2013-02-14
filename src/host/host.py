from control.network import Listener
from model.main_model import Model
import util
import sys
import os

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print "Host: Starting!"
		pyplib = os.path.join(os.environ['pyp'],'src','share')
		sys.path.insert(0,pyplib)
		util.make_logger()
		model = Model(100)
		listener = Listener()
		listener.listen_for_requests(model)
		print "Host: Exiting!"
	elif sys.argv[1] == 'c':
		util.clear_saves()
		print "Host: Cleared all saves!"
