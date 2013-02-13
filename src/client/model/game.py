from pyplib.xml_parser import parse_element
from model.player import Player_Container
from model.control_state import Control_State

class Game:
	def __init__(self,element):
		self.me = Player_Container(parse_element(element,'me'))
		self.them = Player_Container(parse_element(element,'them'))
		self.control_state = Control_State(parse_element(element,'control_state'))
