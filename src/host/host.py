from control.network import Listener
from model.main_model import Model
import util
import sys

if __name__ == '__main__':
	if len(sys.argv) == 1:
		util.make_logger()
		model = Model(100)
		listener = Listener()
		listener.listen_for_requests(model)
	elif sys.argv[1] == 'c':
		util.clear_saves()
