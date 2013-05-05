import sys
import os

pplib = os.path.join(os.environ['postprompt'],'lib','python')
sys.path.insert(0,pplib)
from pplib import util

from control.network import Listener
from model.main_model import Model

if __name__ == '__main__':
	print "Host: Starting!"
	util.make_logger('host')
	model = Model(100)
	listener = Listener()
	listener.listen_for_requests(model)
	print "Host: Exiting!"
