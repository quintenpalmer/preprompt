from pplib import json_parser

from card_list import Card_List

class Collection:
	def __init__(self,obj):
		self.deck    = Card_List(json_parser.get_object(obj,'deck'))
		self.hand    = Card_List(json_parser.get_object(obj,'hand'))
		self.active  = Card_List(json_parser.get_object(obj,'active'))
		self.grave   = Card_List(json_parser.get_object(obj,'grave'))
		self.special = Card_List(json_parser.get_object(obj,'special'))
