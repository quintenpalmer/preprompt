from src.view.view import View
from src.control.network.network_client import Requester
import time

if __name__ == '__main__':
	view = View()
	requester = Requester()
	for i in range(4):
		print requester.send_request('test')
		time.sleep(.5)
	print requester.send_request('exit')
