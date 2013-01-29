import time
from src.control.network.network_client import send_request
from src.view.game_drawer import draw_game

class View:
	def __init__(self,model):
		self.model = model
	def do(self,param):
		ret = send_request(param)
		time.sleep(.01)
		return ret
	def run(self):
		command = ''
		while command != 'exit':
			command = raw_input("Type a command to go: ")
			if command == 'example':
				self.example_start()
			else:
				print self.do(command)
			draw_game(self.model.current_game)
	def example_start(self):
		self.do('test')
		gid,status = self.do('new 26 0 13 1').split(' ')
		self.model.add_game(gid,status)
		self.do('setup '+gid+' 26')
		self.do('draw '+gid+' 26')
		self.do('phase '+gid+' 26')
		self.do('phase '+gid+' 26')
		self.do('play '+gid+' 26 1 0 13 2 0')
		self.do('play '+gid+' 26 1 0 13 2 0')
		self.do('phase '+gid+' 26')
		self.do('turn '+gid+' 26')
		self.do('draw '+gid+' 13')
		self.do('phase '+gid+' 13')
		self.do('phase '+gid+' 13')
		self.do('play '+gid+' 13 1 0 13 2 0')
		self.do('play '+gid+' 13 1 0 13 2 0')
		self.do('phase '+gid+' 13')
		self.do('turn '+gid+' 13')
		self.do('out '+gid+' 26')
