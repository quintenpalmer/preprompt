from src.model.clist import cltypes
from src.model.clist.CardList import CardList
from src.model.player import PlayerType

class Collection:
	def __init__(self,cards=None):
		self.lists = []
		self.visibility = cltypes.Visibility()
		for i in xrange(0,cltypes.size):
			self.lists.append(CardList())
		if cards != None:
			self.lists[cltypes.deck] = CardList(cards)

	def xmlOutput(self,playerType):
		if playerType == PlayerType.me:
			index = 0
		elif playerType == PlayerType.them:
			index = 1
		outStr = ""
		outStr += "<lists>"
		for i in cltypes.full:
			outStr += "<"+cltypes.names[i]+">"
			full = self.visibility.visible[i][index]
			outStr += self.lists[i].xmlOutput(full)
			outStr += "</"+cltypes.names[i]+">"
		outStr += "</lists>"
		return outStr

	def draw(self):
		card = self.lists[cltypes.deck].pop()
		self.lists[cltypes.hand].push(card)
