from pplib import json_parser

from player import Player_Container
from control_state import Control_State

class Game:
	def __init__(self,obj):
		self.me = Player_Container(json_parser.get_object(obj,'me'))
		self.them = Player_Container(json_parser.get_object(obj,'them'))
		self.control_state = Control_State(json_parser.get_object(obj,'controlState'))
