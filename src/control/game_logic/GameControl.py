from src.model.player import PlayerType
from src.control.game_logic.Action import Action
from src.control.game_logic.Action import SubAction

class GameControl:
	def __init__(self,game):
		self.game = game

	def draw(self,uid):
		player = self.game.getMeFromUid(uid)
		player.collection.draw()

	def play(self,playArgs):
		me = self.game.getMeFromUid(playArgs.srcUid)
		cardEffect = me.collection.lists[playArgs.srcList].cards[playArgs.srcCard].effect
		action = Action()
		action.addAction(self.game,playArgs.srcUid,cardEffect.instants)
		#action.accountForBoard()
		#TODO SEND TGT PARAMETERS TO ACTION
		action.act()

	def phase(self):
		pass

	def turn(self):
		pass
