from src.model.card.Card import Card
from src.model.player import Player_Type
from src.model.card import Empty_Card

class Card_List:
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
				outStr += Empty_Card.xmlOutput()
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
