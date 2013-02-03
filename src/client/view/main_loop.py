from pyplib.client_host import *
from view.drawer import draw,init_screen

class Main_Loop:
	def __init__(self,model):
		self.model = model
		init_screen()
	def run(self):
		self.current_message = 'Welcome!'
		command = ''
		while command != 'exit':
			draw(self.model,self.current_message)
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
				self.current_message = 'Not a valid command: '+command
	def request_new(self,me_did=0,them_uid=13,them_did=1):
		resp = request_new(self.model.logged_in_uid,me_did,them_uid,them_did)
		self.current_message = self.model.update_game(resp)
	def request_setup(self):
		resp = request_setup(self.model.current_game_id,self.model.logged_in_uid)
		self.current_message = self.model.update_game(resp)
	def request_draw(self):
		resp = request_draw(self.model.current_game_id,self.model.logged_in_uid)
		self.current_message = self.model.update_game(resp)
	def request_phase(self):
		resp = request_phase(self.model.current_game_id,self.model.logged_in_uid)
		self.current_message = self.model.update_game(resp)
	def request_turn(self):
		resp = request_turn(self.model.current_game_id,self.model.logged_in_uid)
		self.current_message = self.model.update_game(resp)
	def request_play(self,src_list=1,src_card=0,target_uid=13,target_list=2,target_card=0):
		resp = request_play(self.model.current_game_id,self.model.logged_in_uid,src_list,src_card,target_uid,target_list,target_card)
		self.current_message = self.model.update_game(resp)
	def request_test(self):
		resp = request_test(self.model.version)
		self.current_message = resp
	def request_exit(self):
		resp = request_exit(0)
		self.current_message = resp
	def request_out(self):
		resp = request_out(self.model.current_game_id,self.model.logged_in_uid)
		self.current_message = self.model.update_game(resp)
	def example_start(self):
		self.request_test()
		self.request_new()
		self.request_setup()
		self.request_draw()
		self.request_phase()
		self.request_phase()
		self.request_play()
		self.request_play()
		self.request_phase()
		self.request_turn()
		print '*'*50
		print 'SWAPPING PLAYERS'
		print '*'*50
		self.model.logged_in_uid = self.model.get_current_game().them.player.uid
		self.request_out()
		self.request_draw()
		self.request_phase()
		self.request_phase()
		self.request_play(target_uid=26)
		self.request_play(target_uid=26)
		self.request_phase()
		self.request_turn()
