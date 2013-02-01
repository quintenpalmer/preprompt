
import socket
from src import util
host = 'localhost'
port = 52690

request_mappings = {}

def send_request(request):
	s = socket.socket()
	s.connect((host,port))

	s.send(request)
	util.logger.info('Sent request')
	response = s.recv(16384)
	util.logger.info('Received response')
	s.close()
	return response

def request_test():
	pass
def request_new(current_game):
	pass
def request_draw(current_game):
	pass
def request_phase(current_game):
	pass
def request_turn(current_game):
	pass
def request_play(current_game,play_args):
	pass
