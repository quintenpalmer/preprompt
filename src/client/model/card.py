from pplib import json_parser

class Card:
	def __init__(self,obj):
		card_type = json_parser.get_string(obj,'card')
		if card_type == 'full':
			self.name = json_parser.get_string(card_type,'name')
		else:
			self.name = card_type
