from random import randint

from src.model.errors import Game_Action_Error

class phase:
	draw = 0
	pre = 1
	main = 2
	post = 3

	first = draw
	last = post
	all_phases = [draw,pre,main,post]

class super_phase:
	setup = 0
	main = 1
	end = 2

class Control_State:
	def __init__(self,num_players):
		self.players = range(num_players)
		self.super_phase = super_phase.setup
		self.phase = phase.first
		self.turn_owner = self.decide_first_player()
	def step_phase(self):
		self.phase += 1
		if self.phase > phase.last:
			self.phase = phase.last
			raise Game_Action_Error("Phase went past the last one")
	def toggle_turn(self,num_players):
		if self.phase == phase.post:
			self.turn_owner += 1
			if self.turn_owner >= num_players: 
				self.turn_owner = 0
			self.phase = phase.draw
		else:
			raise Game_Action_Error("Can only end your turn during the post phase")
	def exit_setup_phase(self):
		if self.super_phase == super_phase.setup:
			self.super_phase = super_phase.main
		else:
			raise Game_Action_Error("Can only be performed in setup super phase")
			

	def is_given_phase(self,given_phase):
		return self.phase==given_phase
	def decide_first_player(self):
		who = randint(0,1)
		who = 0
		return who
