import time
from src.control.network import send_request
from src.view.game_drawer import draw_game
from xml.dom.minidom import parseString

class View:
	def __init__(self,model):
		self.model = model
	def do(self,param):
		resp = send_request(param)
		time.sleep(.01)
		if param[:3] == 'out':
			self.model.update_game(resp)
		#print '\n'.join(parseString(resp).toprettyxml(indent='  ').split('\n')[1:][:-1])
		return resp
	def run(self):
		command = ''
		while command != 'exit':
			command = raw_input("Type a command to go: ")
			if command == 'example':
				self.example_start()
			elif len(command) >= 4 and command[:4] == 'eval':
				print eval(command[5:])
			else:
				self.do(command)
			draw_game(self.model.current_game[1])
	def example_start(self):
		self.do('test')
		resp = self.do('new 26 0 13 1')
		self.model.add_game(resp)
		gid = str(self.model.current_game[0])
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
