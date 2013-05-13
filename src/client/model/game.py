from pplib import json_parser

from player import Player_Container

class Game:
	def __init__(self,obj):
		self.me = Player_Container(json_parser.get_object(obj,'me'))
		self.them = Player_Container(json_parser.get_object(obj,'them'))
		self.super_phase = json_parser.get_int(obj,'superPhase')
		self.phase = json_parser.get_int(obj,'phase')
		self.turn_owner = json_parser.get_int(obj,'turnOwner')
		self.has_drawn = json_parser.get_bool(obj,'hasDrawn')
