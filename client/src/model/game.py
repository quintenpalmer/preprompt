from pyplib.xml_parser import parse_xml, parse_element

from src.model.player import Player_Container

class Game:
	def __init__(self,element):
		self.me = Player_Container(parse_element(element,'me'))
		self.them = Player_Container(parse_element(element,'them'))
		pass
