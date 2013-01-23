from src.model.card.card import Card
from src.model.player import player_type
from src.model.card import empty_card

class Card_List:
	def __init__(self,cards=None):
		self.cards = []
		if not cards == None:
			for card in cards:
				self.cards.append(card)

	def xml_output(self,full):
		out_str = ""
		out_str += "<num>"
		out_str += str(len(self.cards))
		out_str += "</num>"
		out_str += "<cards>"
		for card in self.cards:
			out_str += "<card>"
			if full:
				out_str += card.xml_output()
			else:
				out_str += empty_card.xml_output()
			out_str += "</card>"
		out_str += "</cards>"
		return out_str

	def pop(self):
		if len(self.cards) > 0:
			card = self.cards[0]
			self.cards = self.cards[1:]
			return card
		else:
			return None

	def push(self,card):
		self.cards.append(card)
