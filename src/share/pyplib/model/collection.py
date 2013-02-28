from card_list import Card_List
from pyplib.xml_parser import parse_element

class Collection:
	def __init__(self,element):
		self.deck    = Card_List(parse_element(element,'deck'))
		self.hand    = Card_List(parse_element(element,'hand'))
		self.active  = Card_List(parse_element(element,'active'))
		self.grave   = Card_List(parse_element(element,'grave'))
		self.special = Card_List(parse_element(element,'special'))
