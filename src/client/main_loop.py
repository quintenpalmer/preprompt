from pplib.client_host_json import *

from drawer import draw

class Main_Loop:
	def __init__(self,model):
		self.model = model
	def run(self):
		self.current_message = 'Welcome!'
		self.command = ''
		self.last_line_breaks=0
		while self.command != 'exit':
			try:
				self.last_line_breaks = draw(self.model,"Command %s was %s!"%(self.command,self.current_message),self.last_line_breaks)
				self.command = raw_input("Type a command to go: ")
				if self.command == '!!':
					self.command = self.last_command
				self.last_command = self.command
				self.run_command()
			except Exception as e:
				print "error caught"
				#print e.message
	def run_command(self):
		if self.command == 'new':
			me_did=0
			them_uid=2
			them_did=0
			self.resp = request_new(self.model.logged_in_uid,me_did,them_uid,them_did)
			self.current_message = self.model.update_game(self.resp)
		elif self.command == 'test':
			self.resp = request_test(self.model.version)
			self.current_message = self.resp
		elif self.command == 'setup':
			self.resp = request_setup(self.model.current_game_id,self.model.logged_in_uid)
			self.current_message = self.model.update_game(self.resp)
		elif self.command == 'draw':
			self.resp = request_draw(self.model.current_game_id,self.model.logged_in_uid)
			self.current_message = self.model.update_game(self.resp)
		elif self.command == 'phase':
			self.resp = request_phase(self.model.current_game_id,self.model.logged_in_uid)
			self.current_message = self.model.update_game(self.resp)
		elif self.command == 'turn':
			self.resp = request_turn(self.model.current_game_id,self.model.logged_in_uid)
			self.current_message = self.model.update_game(self.resp)
		elif self.command == 'play':
			src_list=1
			src_card=0
			target_uid=13
			target_list=2
			target_card=0
			self.resp = request_play(self.model.current_game_id,self.model.logged_in_uid,src_list,src_card,target_uid,target_list,target_card)
			self.current_message = self.model.update_game(self.resp)
		elif self.command == 'exit':
			self.resp = request_exit(0)
			self.current_message = self.resp
		elif self.command == 'close':
			self.resp = request_close(0)
			self.current_message = self.resp
		elif self.command == 'out':
			self.resp = request_out(self.model.current_game_id,self.model.logged_in_uid)
			self.current_message = self.model.update_game(self.resp)
		elif self.command == 'listall':
			self.resp = request_list(self.model.logged_in_uid)
			self.current_message = self.resp
		elif self.command == 'list':
			self.current_message = str(self.model.games.keys())
		elif self.command == 'stats':
			self.current_message = "me : %s them : %s"%(self.model.get_current_game().me.uid,self.model.get_current_game().them.uid)
		elif self.command[:4] == 'curr':
			try:
				self.model.current_game_id = int(self.command[5:])
			except ValueError:
				self.current_message = 'Invalid gameId %s'%self.command
		elif self.command == 'swap':
			self.model.logged_in_uid = self.model.get_current_game().them.uid
			self.current_message = 'ok'
			self.resp = request_out(self.model.current_game_id,self.model.logged_in_uid)
			self.current_message = self.model.update_game(self.resp)
		elif self.command[:4] == 'help':
			self.current_message = '''Valid commands are:
	test     send a test service
	exit     close the client (and host)
	new      start a new game
	setup    run the setup for the current game
	draw     draw your card (only valid in the draw phase)
	phase    swap to the next phase of your turn
	turn     swap to the other player's turn
	play     play your last card
	out      get the current game from the host
	curr <i> change the current game id to game id <i>
	list     get a list of this client's game_ids
	swap     swap to playing as the other player
					'''
		else:
			self.current_message = 'Not a valid command: ' + self.command
