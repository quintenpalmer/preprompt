from src.model.player.Player_Container import Player_Container
from src.model.player import Player_Type
from src.model.phase.Turn import Turn

class Game:
	def __init__(self,player1=None,player2=None):
		self.players = []
		if player1 != None:
			self.players.append(player1)
		else:
			self.players.append(Player_Container())
		if player2 != None:
			self.players.append(player2)
		else:
			self.players.append(Player_Container())
		self.turn = Turn()

	def getMe_FromUid(self,uid):
		if self.players[0].player.uid == uid:
			return self.players[0]
		elif self.players[1].player.uid == uid:
			return self.players[1]
		else:
			raise Exception("Not the uid of a player playing this game")

	def getThem_FromUid(self,uid):
		if self.players[0].player.uid == uid:
			return self.players[1]
		elif self.players[1].player.uid == uid:
			return self.players[0]
		else:
			raise Exception("Not the uid of a player playing this game")

	def xmlOutput(self,uid):
		outStr = "<game>"
		outStr += "<me>"
		outStr += self.getMe_FromUid(uid).xmlOutput(Player_Type.me)
		outStr += "</me>"
		outStr += "<them>"
		outStr += self.getThem_FromUid(uid).xmlOutput(Player_Type.them)
		outStr += "</them>"
		outStr += "</game>"
		return outStr

