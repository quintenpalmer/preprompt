from src.control.command_sender import build_and_send_request
from src.util import make_logger

if __name__ == '__main__':
	make_logger()
	build_and_send_request('exit',None)
