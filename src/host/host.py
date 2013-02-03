from control.network import Listener
from model.main_model import Model
from util import make_logger

if __name__ == '__main__':
	make_logger()
	model = Model(100)
	listener = Listener()
	listener.listen_for_requests(model)
