from src.control.xml_parser import parse_string, parse_element

class Game:
	def __init__(self,xml_string):
		element = parse_string(xml_string)
		print element
