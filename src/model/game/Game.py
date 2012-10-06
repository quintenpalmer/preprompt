from src.model.player.PlayerContainer import PlayerContainer
from src.model.player import PlayerType

class Game:
	def __init__(self,player1=None,player2=None):
		self.players = []
		if player1 != None:
			self.players.append(player1)
		else:
			self.players.append(PlayerContainer())
		if player2 != None:
			self.players.append(player2)
		else:
			self.players.append(PlayerContainer())

	def getMeFromUid(self,uid):
		if self.players[0].player.uid == uid:
			return self.players[0]
		elif self.players[1].player.uid == uid:
			return self.players[1]
		else:
			raise Exception("Not the uid of a player playing this game")

	def getThemFromUid(self,uid):
		if self.players[0].player.uid == uid:
			return self.players[1]
		elif self.players[1].player.uid == uid:
			return self.players[0]
		else:
			raise Exception("Not the uid of a player playing this game")

	def xmlOutput(self,uid):
		outStr = ""
		outStr += "<me>"
		outStr += self.getMeFromUid(uid).xmlOutput(PlayerType.me)
		outStr += "</me>"
		outStr += "<them>"
		outStr += self.getThemFromUid(uid).xmlOutput(PlayerType.them)
		outStr += "</them>"
		return outStr

