from src.model.card import Card
from pyplib.xml_parser import parse_int, parse_elements

class Card_List:
	def __init__(self,element):
		size = parse_int(element,'num')
		self.cards = []
		for card_element in parse_elements(element,'card'):
			self.cards.append(Card(card_element))

		def __iter__(self):
			return self.cards
