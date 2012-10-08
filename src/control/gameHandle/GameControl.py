from src.model.player import PlayerType
from src.control.gameHandle.Action import Action

class GameControl:
	def __init__(self,game):
		self.game = game

	def draw(self,uid):
		player = self.game.getMeFromUid(uid)
		player.collection.draw()

	def play(self,playReq):
		player = self.game.getMeFromUid(playReq.uid)
		args = playReq.playArgs
		cardEffect = player.collection.lists[playReq.cardList].cards[playReq.cardNum].effect
		action = Action(self.game,playReq.uid,cardEffect)
		action.accountForBoard()
		action.act()
		#uid,i,args = None
		#action = Action(self.getMeFromUid(uid).collection.hand[i].effect,args)
