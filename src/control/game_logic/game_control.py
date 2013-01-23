from src.model.player import player_type
from src.control.game_logic.action import Action
from src.control.game_logic.action import Sub_Action

class Game_Control:
	def __init__(self,game):
		self.game = game

	def draw(self,uid):
		player = self.game.get_me_from_uid(uid)
		player.collection.draw()

	def play(self,play_args):
		if self.game.current_turn_owner == play_args.src_uid:
			me = self.game.get_me_from_uid(play_args.src_uid)
			card_effect = me.collection.lists[play_args.src_list].cards[play_args.src_card].effect
			action = Action()
			action.add_action(self.game,play_args.src_uid,card_effect.instants)
			#action.account_for_board()
			#TODO SEND TGT PARAMETERS TO ACTION
			action.act()
		else:
			raise Exception("Not that player's turn")

	def phase(self):
		pass

	def turn(self):
		pass
