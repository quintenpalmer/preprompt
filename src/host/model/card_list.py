from model.card import Card, Empty_Card
from model import player_type

from model.errors import Game_Action_Error

from pyplib.xml_parser import parse_elements

class Card_List:
	def __init__(self,**kwargs):
		if len(kwargs) == 0:
			self.cards = []
		elif kwargs.has_key('cards'):
			cards = kwargs['cards']
			self.cards = []
			if not cards == None:
				for card in cards:
					self.cards.append(card)
		elif kwargs.has_key('element'):
			element = kwargs['element']
			self.cards = []
			for card_element in parse_elements(element,'card'):
				self.cards.append(Card(element=card_element))
		else:
			raise Game_Action_Error("Card_List was instantiated with improper parameters: %s"%kwargs)

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
