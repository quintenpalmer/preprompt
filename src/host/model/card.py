from pplib.errors import PP_Game_Action_Error
from pplib.xml_parser import parse_string,parse_element

from model.card_effect.effect import Effect

class Card:
	def __init__(self,**kwargs):
		if kwargs.has_key('name') and kwargs.has_key('effect'):
			self.name = kwargs['name']
			self.effect = kwargs['effect']
		elif kwargs.has_key('element'):
			element = kwargs['element']
			card_type = parse_string(element,'type')
			if card_type == 'full':
				self.name = parse_string(element,'name')
				self.effect = Effect(element=parse_element(element,'effect'))
		else:
			raise PP_Game_Action_Error("Card Instantiated without correct args: %s"%kwargs)

	def xml_output(self,full):
		xml = '<type>full</type>'
		xml += '<name>%s</name>'%self.name
		xml += '<effect>%s</effect>'%self.effect.xml_output(full)
		return xml

	def play(self,args):
		self.effect(args)

class Empty_Card:
	def xml_output(self):
		xml = "<type>Unknown</type>"
		return xml
