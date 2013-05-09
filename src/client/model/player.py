from pplib import json_parser

from collection import Collection

class Player_Container:
	def __init__(self,obj):
		self.uid = json_parser.get_int(obj,'uid')
		self.name = json_parser.get_string(obj,'name')
		self.health = json_parser.get_int(obj,'health')
		self.collection = Collection(json_parser.get_object(obj,'deck'))
