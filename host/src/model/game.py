from src.model.player import Player_Container
from src.model.player import player_type
from src.model.control_state import Control_State,super_phase

from src.control.game_logic.action import Action

class Game_Action_Error(Exception):
	def __init__(self,message):
		self.message = message
	def __str__(self):
		return self.message

class Game:
	def __init__(self,player1,player2):
		self.players = []
		self.players.append(player1)
		self.players.append(player2)
		self.control_state = Control_State(len(self.players))

	def get_me_from_uid(self,uid):
		if self.players[0].player.uid == uid:
			return self.players[0]
		elif self.players[1].player.uid == uid:
			return self.players[1]
		else:
			raise Game_Action_Error("Not the uid of a player playing this game:"+str(uid))

	def get_them_from_uid(self,uid):
		if self.players[0].player.uid == uid:
			return self.players[1]
		elif self.players[1].player.uid == uid:
			return self.players[0]
		else:
			raise Game_Action_Error("Not the uid of a player playing this game:"+str(uid))

	def get_current_turn_owner(self):
		return self.players[self.control_state.turn_owner].player.uid

	def xml_output(self,uid):
		out_str = "<game>"
		out_str += "<me>"
		out_str += self.get_me_from_uid(uid).xml_output(player_type.me)
		out_str += "</me>"
		out_str += "<them>"
		out_str += self.get_them_from_uid(uid).xml_output(player_type.them)
		out_str += "</them>"
		out_str += "</game>"
		return out_str

	def __repr__(self):
		return "Game: Player:"+self.players[0].player.name+" Player:"+self.players[1].player.name+" State:"+str(self.control_state.phase)

	def setup(self):
		self.verify_setup_super_phase('setup')
		for player in self.players:
			for i in range(5):
				player.collection.draw()
		self.control_state.exit_setup_phase()

	def draw(self,uid):
		self.verify_main_super_phase('draw')
		if self.get_current_turn_owner() == uid:
			self.get_me_from_uid(uid).collection.draw()
		else:
			raise Game_Action_Error("Player cannot conduct draw during this turn")

	def play(self,play_args):
		self.verify_main_super_phase('play')
		if self.get_current_turn_owner() == play_args.src_uid:
			me = self.get_me_from_uid(play_args.src_uid)
			card_effect = me.collection.lists[play_args.src_list].cards[play_args.src_card].effect
			if self.control_state.is_given_phase(card_effect.instants.valid_phase):
				action = Action()
				action.add_action(self,play_args.src_uid,card_effect.instants)
				#action.account_for_board()
				#TODO SEND TGT PARAMETERS TO ACTION
				success = action.act()
				if card_effect.persists.does_persist and success:
					me.collection.play_to_active(play_args.src_card)
				else:
					me.collection.play_to_grave(play_args.src_card)
			else:
				raise Game_Action_Error("Not the correct phase to play that card")
		else:
			raise Game_Action_Error("Not that correct turn for that player to play that card")

	def step_phase(self):
		self.verify_main_super_phase('phase')
		self.control_state.step_phase()

	def toggle_turn(self):
		self.verify_main_super_phase('turn')
		self.control_state.toggle_turn(len(self.players))

	def verify_main_super_phase(self,action):
		if not self.control_state.super_phase == super_phase.main:
			raise Game_Action_Error("%s can only be performed in the regular gameplay super phase"%(action,))

	def verify_setup_super_phase(self,action):
		if not self.control_state.super_phase == super_phase.setup:
			raise Game_Action_Error("%s can only be performed in the setup super phase"%(action,))
