from src.control.xml_parser import parse_string

class Card:
	def __init__(self,element):
		card_type = parse_string(element,'type')
		if card_type == 'full':
			self.name = parse_string(element,'name')
		else:
			self.name = card_type
