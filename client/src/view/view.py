from src.control.command_sender import build_and_send_request

class View:
	def __init__(self,model):
		self.model = model
	def run(self):
		self.request_new()
		command = ''
		while command != 'exit':
			command = raw_input("Type a command to go: ")
			if command == 'example':
				self.example_start()
			elif command == 'new':
				self.request_new()
			elif command == 'test':
				self.request_test()
			elif command == 'setup':
				self.request_setup()
			elif command == 'draw':
				self.request_draw()
			elif command == 'phase':
				self.request_phase()
			elif command == 'turn':
				self.request_turn()
			elif command == 'play':
				self.request_play()
			elif command == 'exit':
				self.request_exit()
			elif len(command) >= 4 and command[:4] == 'eval':
				print eval(command[5:])
			elif command == 'swap':
				self.model.logged_in_uid = self.model.get_current_game().them.player.uid
				self.request_out()
			else:
				print 'not a valid command'
	def request_new(self):
		build_and_send_request('new',self.model,[self.model.logged_in_uid,0,13,1])
	def request_setup(self):
		build_and_send_request('setup',self.model)
	def request_draw(self):
		build_and_send_request('draw',self.model)
	def request_phase(self):
		build_and_send_request('phase',self.model)
	def request_turn(self):
		build_and_send_request('turn',self.model)
	def request_play(self):
		build_and_send_request('play',self.model,[1,0,13,2,0])
	def request_test(self):
		build_and_send_request('test',self.model)
	def request_exit(self):
		build_and_send_request('exit',self.model)
	def request_out(self):
		build_and_send_request('out',self.model)
	def example_start(self):
		build_and_send_request('test',self.model)
		build_and_send_request('new',self.model,[26,0,13,1])
		build_and_send_request('setup',self.model)
		build_and_send_request('draw',self.model)
		build_and_send_request('phase',self.model)
		build_and_send_request('phase',self.model)
		build_and_send_request('play',self.model,[1,0,13,2,0])
		build_and_send_request('play',self.model,[1,0,13,2,0])
		build_and_send_request('phase',self.model)
		build_and_send_request('turn',self.model)
		self.model.logged_in_uid = self.model.get_current_game().them.player.uid
		self.request_out()
		build_and_send_request('draw',self.model)
		build_and_send_request('phase',self.model)
		build_and_send_request('phase',self.model)
		build_and_send_request('play',self.model,[1,0,13,2,0])
		build_and_send_request('play',self.model,[1,0,13,2,0])
		build_and_send_request('phase',self.model)
		build_and_send_request('turn',self.model)
		build_and_send_request('out',self.model)
