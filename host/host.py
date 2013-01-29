from src.control.network.network_host import Listener
from src.model.model import Model
#from src.view import Display

if __name__ == '__main__':
	model = Model()
	listener = Listener()
	listener.listen_for_requests(model)
