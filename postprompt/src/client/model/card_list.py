from model.card import Card
from pyplib.xml_parser import parse_elements

class Card_List:
	def __init__(self,element):
		self.cards = []
		for card_element in parse_elements(element,'card'):
			self.cards.append(Card(card_element))
