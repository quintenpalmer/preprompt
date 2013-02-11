from pyplib.xml_parser import parse_int, parse_bool

class Control_State:
	def __init__(self,element):
		self.super_phase = parse_int(element,'super_phase')
		self.phase = parse_int(element,'phase')
		self.turn_owner = parse_int(element,'turn_owner')
		self.has_drawn = parse_bool(element,'has_drawn')
