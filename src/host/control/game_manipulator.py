from pyplib.errors import PP_Game_Action_Error
from model.control_state import phase
from model.action import Action

class Manipulator:
	def __init__(self,game):
		self.game = game

	def setup(self):
		self.game.verify_setup_super_phase('setup')
		for player in self.game.players:
			for i in range(5):
				player.collection.draw()
		self.game.control_state.exit_setup_phase()

	def draw(self,uid):
		self.game.verify_main_super_phase('draw')
		self.game.verify_current_turn_owner(uid,'draw')
		if self.game.control_state.is_given_phase(phase.draw):
			if not self.game.control_state.has_drawn:
				self.game.get_me_from_uid(uid).collection.draw()
				self.game.control_state.has_drawn = True
			else:
				raise PP_Game_Action_Error("Player has already drawn their card")
		else:
			raise PP_Game_Action_Error("Can only draw during the draw phase")

	def play(self,play_args):
		self.game.verify_main_super_phase('play')
		self.game.verify_current_turn_owner(play_args.src_uid,'play')
		me = self.game.get_me_from_uid(play_args.src_uid)
		try:
			card_effect = me.collection.lists[play_args.src_list].cards[play_args.src_card].effect
		except IndexError:
			raise PP_Game_Action_Error("There are no more cards in that player's %s"%(play_args.src_list,))
		if self.game.control_state.is_given_phase(card_effect.instants.valid_phase):
			action = Action()
			action.add_action(self.game,play_args.src_uid,card_effect.instants)
			#action.account_for_board()
			#TODO SEND TGT PARAMETERS TO ACTION
			success = action.act()
			if card_effect.persists.does_persist and success:
				me.collection.play_to_active(play_args.src_card)
			else:
				me.collection.play_to_grave(play_args.src_card)
		else:
			raise PP_Game_Action_Error("Not the correct phase to play that card")

	def step_phase(self,uid):
		self.game.verify_current_turn_owner(uid,'phase')
		self.game.verify_main_super_phase('phase')
		self.game.control_state.step_phase()

	def toggle_turn(self,uid):
		self.game.verify_current_turn_owner(uid,'turn')
		self.game.verify_main_super_phase('turn')
		#for card in self.player.collection.active
		self.game.control_state.toggle_turn(len(self.game.players))
