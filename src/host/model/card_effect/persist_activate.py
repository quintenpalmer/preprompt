from pyplib.xml_parser import parse_elements,parse_element
from model.errors import Game_Action_Error

class Persist_Activate_list:
	def __init__(self,**kwargs):
		if kwargs.has_key('pactivates'):
			self.persist_activates = kwargs['pactivates']
		elif kwargs.has_key('element'):
			element = kwargs['element']
			self.persist_activates = []
			for ele in parse_elements(element,'pactivate'):
				self.persist_activates.append(Persist_Activate(element=ele))
		else:
			raise Game_Action_Error("Persist_Actiate_List instantiated with invalid constructor %s"%kwargs.keys())

	def on_act(self,action,card_owner):
		for pactivate in self.persist_activates:
			pactivate.on_act(action,card_owner)

	def xml_output(self):
		xml = ''
		for pactivate in self.persist_activates:
			xml += '<pactivate>%s</pactivate>'%pactivate.xml_output()
		return xml

class Persist_Activate:
	def __init__(self,**kwargs):
		if kwargs.has_key('effect') and kwargs.has_key('conds'):
			self.effect = kwargs['effect']
			self.conds = kwargs['conds']
		elif kwargs.has_key('element'):
			element = kwargs['element']
			#TODO parse the correct effects and conds
			self.effect = None
			self.conds = []
			for ele in parse_elements(element,'cond'):
				self.conds.append(None)
		else:
			raise Game_Action_Error("Persist_Actiate instantiated with invalid constructor %s"%kwargs.keys())


	def on_act(self,action,card_owner):
		if self.is_valid(action,card_owner):
			self.effect.apply_to(action)

	def is_valid(self,action,card_owner):
		valid = True
		for cond in self.conds:
			valid = valid and cond.is_valid(action,card_owner)
		return valid

	def xml_output(self):
		xml = '<effect>%s</effect>'%self.effect.xml_output()
		for cond in self.conds:
			xml += '<cond>%s</cond>'%cond.xml_output()
		return xml
