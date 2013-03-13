from pyplib.errors import PP_Game_Action_Error
from model.collection import Collection

from pyplib.xml_parser import parse_element, parse_string, parse_int

class Player_Container:
	def __init__(self,**kwargs):
		if kwargs.has_key('player') and kwargs.has_key('collection'):
			player = kwargs['player']
			collection = kwargs['collection']
			self.player = player
			self.collection = collection
		elif kwargs.has_key('element'):
			element = kwargs['element']
			self.player = Player(element=parse_element(element,'player'))
			self.collection = Collection(element=parse_element(element,'collection'))
		else:
			raise PP_Game_Action_Error("Game Instantiated without correct args")

	def xml_output(self,player_type):
		xml = '<player>%s</player>'%self.player.xml_output(player_type)
		xml += '<collection>%s</collection>'%self.collection.xml_output(player_type)
		return xml

class Player:
	def __init__(self,**kwargs):
		if kwargs.has_key('uid') and kwargs.has_key('name'):
			self.uid = kwargs['uid']
			self.name = kwargs['name']
			self.health = 50
		elif kwargs.has_key('element'):
			element = kwargs['element']
			self.uid = parse_int(element,'uid')
			self.name = parse_string(element,'name')
			self.health = parse_int(element,'health')

	def xml_output(self,player_type):
		xml = '<uid>%s</uid>'%str(self.uid)
		xml += '<name>%s</name>'%self.name
		xml += '<health>%s</health>'%str(self.health)
		return xml
