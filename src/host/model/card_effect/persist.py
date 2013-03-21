from pyplib.xml_parser import parse_element,parse_elements,parse_bool,parse_string
from pyplib.errors import PP_Game_Action_Error

from control.lstructs import get_effect_from_xml_name

class Persist_Cond_list:
	def __init__(self,**kwargs):
		if kwargs.has_key('does_persist') and kwargs.has_key('conds'):
			self.does_persist = kwargs['does_persist']
			self.conds = kwargs['conds']
		elif kwargs.has_key('element'):
			element = kwargs['element']
			self.does_persist = parse_bool(element,'does_persist')
			self.conds = []
			for ele in parse_elements(element,'cond'):
				name = parse_string(ele,'name')
				self.conds.append(get_effect_from_xml_name(name)(element=ele))
		else:
			raise PP_Game_Action_Error("Persist_Cond_List instantiated with invalid constructor %s"%kwargs.keys())

	def tick(self,game,uid):
		for cond in self.conds:
			cond.tick(game,uid)

	def persists(self,game,uid):
		does_persist = self.does_persist
		for cond in self.conds:
			does_persist = does_persist and cond.persists
		return does_persist

	def reset(self,game,uid):
		for cond in self.conds:
			cond.reset(game,uid)

	def xml_output(self,full):
		xml = '<does_persist>%s</does_persist>'%str(self.does_persist)
		for cond in self.conds:
			xml += '<cond>%s</cond>'%cond.xml_output(full)
		return xml
