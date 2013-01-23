from src.model.player import Player_Type
from src.control.game_logic.Action import Action
from src.control.game_logic.Action import Sub_Action

class Game_Control:
	def __init__(self,game):
		self.game = game

	def draw(self,uid):
		player = self.game.getMe_FromUid(uid)
		player.collection.draw()

	def play(self,playArgs):
		me = self.game.getMe_FromUid(playArgs.srcUid)
		cardEffect = me.collection.lists[playArgs.srcList].cards[playArgs.srcCard].effect
		action = Action()
		action.addAction(self.game,playArgs.srcUid,cardEffect.instants)
		#action.accountFor_Board()
		#TODO SEND TGT PARAMETERS TO ACTION
		action.act()

	def phase(self):
		pass

	def turn(self):
		pass
