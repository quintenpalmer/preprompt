from pplib import json_parser

from card_list import Card_List

class Player_Container:
	def __init__(self,obj):
		self.uid = json_parser.get_int(obj,'uid')
		self.name = json_parser.get_string(obj,'name')
		self.health = json_parser.get_int(obj,'health')
		self.deck    = Card_List(json_parser.get_object(obj,'deck'))
		self.hand    = Card_List(json_parser.get_object(obj,'hand'))
		self.active  = Card_List(json_parser.get_object(obj,'active'))
		self.grave   = Card_List(json_parser.get_object(obj,'grave'))
		self.special = Card_List(json_parser.get_object(obj,'special'))
