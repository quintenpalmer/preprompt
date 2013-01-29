from src.control.network.network_host import Listener
from src.model.model import Model
from util import make_logger
#from src.view import Display

if __name__ == '__main__':
	#logging.basicConfig(filename='log/pyphost.log',format='%(asctime)s %(levelname)s:\t%(message)s',level=logging.DEBUG)
	make_logger()
	model = Model()
	listener = Listener()
	listener.listen_for_requests(model)
