from src.model.card import Card, Empty_Card
from src.model.player import player_type

class Card_List:
	def __init__(self,cards=None):
		self.cards = []
		if not cards == None:
			for card in cards:
				self.cards.append(card)

	def xml_output(self,full):
		xml = '<cards>'
		for card in self.cards:
			xml += '<card>'
			if full:
				xml += card.xml_output()
			else:
				xml += Empty_Card().xml_output()
			xml += '</card>'
		xml += '</cards>'
		return xml

	def pop(self,index=-1):
		return self.cards.pop(index)

	def push(self,card):
		self.cards.append(card)
