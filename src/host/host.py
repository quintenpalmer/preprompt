import sys
import os

from pyplib import util

from control.network import Listener
from model.main_model import Model

if __name__ == '__main__':
	print "Host: Starting!"
	pyplib = os.path.join(os.environ['pyp'],'src','share')
	sys.path.insert(0,pyplib)
	util.make_logger('host')
	model = Model(100)
	listener = Listener()
	listener.listen_for_requests(model)
	print "Host: Exiting!"
