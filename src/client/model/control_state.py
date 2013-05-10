from pplib import json_parser

class Control_State:
	def __init__(self,obj):
		self.super_phase = json_parser.get_int(obj,'superPhase')
		self.phase = json_parser.get_int(obj,'phase')
		self.turn_owner = json_parser.get_int(obj,'turnOwner')
		self.has_drawn = json_parser.get_bool(obj,'hasDrawn')
