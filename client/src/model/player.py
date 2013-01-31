from src.model.collection import Collection
from src.control.xml_parser import parse_element, parse_string, parse_int

class Player_Container:
	def __init__(self,element):
		self.player = Player(parse_element(element,'player'))
		self.collection = Collection(parse_element(element,'collection'))

class Player:
	def __init__(self,element):
		self.uid = parse_int(element,'uid')
		self.name = parse_string(element,'name')
		self.health = parse_int(element,'health')
