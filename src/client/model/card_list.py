from pplib import json_parser

from card import Card

class Card_List:
	def __init__(self,obj):
		self.cards = []
		for card_element in json_parser.get_objects(obj,'cards'):
			self.cards.append(Card(card_element))
