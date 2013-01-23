from src.model.clist import cltypes
from src.model.clist.Card_List import Card_List
from src.model.player import Player_Type

class Collection:
	def __init__(self,cards=None):
		self.lists = []
		self.visibility = cltypes.Visibility()
		for i in xrange(0,cltypes.size):
			self.lists.append(Card_List())
		if cards != None:
			self.lists[cltypes.deck] = Card_List(cards)

	def xmlOutput(self,playerType):
		if playerType == Player_Type.me:
			index = 0
		elif playerType == Player_Type.them:
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
