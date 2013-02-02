
from src.control.network import send_request
from src.util import make_logger

if __name__ == '__main__':
	make_logger()
	request = '<request'
	print send_request(request)
