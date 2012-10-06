from src.model.card.Card import Card
from src.model.player import PlayerType
from src.model.card import EmptyCard

class CardList:
	def __init__(self,cards=None):
		self.cards = []
		if not cards == None:
			for card in cards:
				self.cards.append(card)

	def xmlOutput(self,full):
		outStr = ""
		outStr += "<num>"
		outStr += str(len(self.cards))
		outStr += "</num>"
		outStr += "<cards>"
		for card in self.cards:
			outStr += "<card>"
			if full:
				outStr += card.xmlOutput()
			else:
				outStr += EmptyCard.xmlOutput()
			outStr += "</card>"
		outStr += "</cards>"
		return outStr

	def pop(self):
		if len(self.cards) > 0:
			card = self.cards[0]
			self.cards = self.cards[1:]
			return card
		else:
			return None

	def push(self,card):
		self.cards.append(card)
