from pplib import json_parser

class Card:
	def __init__(self,obj):
		card = json_parser.get_object(obj,'card')
		self.name = json_parser.get_string(card,'name')
