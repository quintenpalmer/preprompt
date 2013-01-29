
from src.control.network.network_client import Requester

if __name__ == '__main__':
	requester = Requester()
	requester.send_request('exit')
