from src.control.xml_parser import parse_xml, parse_element

from src.model.player.player_container import Player_Container

class Game:
	def __init__(self,element):
		self.me = Player_Container(parse_element(element,'me'))
		self.them = Player_Container(parse_element(element,'them'))
		pass
