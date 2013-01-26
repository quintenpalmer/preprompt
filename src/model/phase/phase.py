from random import randint

draw = 0
pre = 1
main = 2
post = 3

first = draw
last = post
all_phases = [draw,pre,main,post]

class Phase:
	def __init__(self,num_players):
		self.players = range(num_players)
		self.current_phase = draw
		self.current_turn_owner = self.decide_first_player()
	def change_phase(self):
		self.current_phase += 1
		if self.current_phase > last:
			raise Exception("Phase went past the last one")
	def change_turn(self,num_players):
		if self.current_phase == post:
			self.current_turn_owner += 1
			if self.current_turn_owner > num_players: 
				self.current_turn_owner = 0
		else:
			raise Exception("Can only end your turn during the post phase")
	def is_given_phase(self,given_phase):
		return self.current_phase==given_phase
	def decide_first_player(self):
		who = randint(0,1)
		who = 0
		return who
