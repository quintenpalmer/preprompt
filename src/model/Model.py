from src.control import databaseReader
from src.control.gameHandle.GameControl import GameControl

class Model:
	def __init__(self,tmp):
		self.games = {}
		self.freeIds = range(0,100)

	def startGame(self,startInfo):
		game = databaseReader.getGame(startInfo)
		gameId = self.popId()
		self.games[gameId] = GameControl(game)
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
			print val.game.xmlOutput(uid)
