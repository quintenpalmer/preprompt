from src.control.network import Listener
from src.model.model import Model
from src.util import make_logger
#from src.view import Display

if __name__ == '__main__':
	make_logger()
	model = Model(1)
	listener = Listener()
	listener.listen_for_requests(model)
