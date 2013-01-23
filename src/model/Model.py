from src.control.load import database_reader
from src.control.game_logic.Game_Control import Game_Control

class Model:
	def __init__(self):
		self.games = {}
		self.freeIds = range(0,100)

	def startGame(self,config_args):
		game = database_reader.getGame(config_args)
		gameId = self.popId()
		self.games[gameId] = Game_Control(game)
		return gameId

	def stopGame(self,gameId):
		del self.games[gameId]
		self.pushId(gameId)

	def popId(self):
		if len(self.freeIds) > 0:
			return self.freeIds.pop(0)
		else:
			raise Exception("No room for more games")

	def pushId(self,pushId):
		self.freeIds.append(pushId)

	def out(self,uid):
		for val in self.games.itervalues():
			return val.game.xmlOutput(uid)
