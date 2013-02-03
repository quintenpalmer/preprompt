from model.errors import Game_Action_Error

from pyplib.xml_parser import parse_string

class Card:
	def __init__(self,**kwargs):
		if kwargs.has_key('name') and kwargs.has_key('effect'):
			self.name = kwargs['name']
			self.effect = kwargs['effect']
		elif kwargs.has_key('element'):
			#TODO need to flatten effect if a full card flattening
			element = kwargs['element']
			card_type = parse_string(element,'type')
			if card_type == 'full':
				self.name = parse_string(element,'name')
		else:
			raise Game_Action_Error("Card Instantiated without correct args: %s"%kwargs)

	def xml_output(self):
		xml = '<type>full</type>'
		xml += '<name>%s</name>'%self.name
		return xml

	def play(self,args):
		self.effect(args)

class Empty_Card:
	def xml_output(self):
		xml = "<type>empty</type>"
		return xml
