from pyplib.xml_parser import parse_elements,parse_element,parse_int,parse_string
from model.errors import Game_Action_Error
from control.load.lstructs import get_effect_from_xml_name

class Instant_List:
	def __init__(self,**kwargs):
		if kwargs.has_key('instants') and kwargs.has_key('valid_phase'):
			self.instants = kwargs['instants']
			self.valid_phase = kwargs['valid_phase']
		elif kwargs.has_key('element'):
			element = kwargs['element']
			self.instants = []
			for ele in parse_elements(element,'instant'):
				self.instants.append(Instant(element=ele))
			self.valid_phase = parse_int(element,'valid_phase')
		else:
			raise Game_Action_Error("Instant_List instantiated with invalid constructor %s"%kwargs.keys())

	def apply_to(self,action):
		for instant in self.instants:
			instant.apply_to(action)

	def xml_output(self):
		xml = '<valid_phase>%s</valid_phase>'%str(self.valid_phase)
		for instant in self.instants:
			xml += '<instant>%s</instant>'%instant.xml_output()
		return xml

class Instant:
	def __init__(self,**kwargs):
		if kwargs.has_key('effect') and kwargs.has_key('conds'):
			self.effect = kwargs['effect']
			self.conds = kwargs['conds']
		elif kwargs.has_key('element'):
			element = kwargs['element']
			#TODO parse the correct effects and conds
			effect_element = parse_element(element,'effect')
			name = parse_string(effect_element,'name')
			self.effect = get_effect_from_xml_name(name)(element=effect_element)
			self.conds = []
			for ele in parse_elements(element,'cond'):
				name = parse_string(ele,'name')
				self.conds.append(get_effect_from_xml_name(name)(element=ele))
		else:
			raise Game_Action_Error("Instant instantiated with invalid constructor %s"%kwargs.keys())

	def is_valid(self,action):
		valid = True
		for cond in self.conds:
			valid = valid and cond.is_valid(action)
		return valid

	def apply_to(self,action):
		if self.is_valid(action):
			self.effect.apply_to(action)

	def xml_output(self):
		xml = '<effect>%s</effect>'%self.effect.xml_output()
		for cond in self.conds:
			xml += '<cond>%s</cond>'%cond.xml_output()
		return xml
