from pyplib.errors import PP_Game_Action_Error
from pyplib.xml_parser import parse_string,parse_element,parse_elements

from model.card_effect.instant import Instant_List
from model.card_effect.persist import Persist_Cond_list
from model.card_effect.persist_activate import Persist_Activate_list

class Effect:
	def __init__(self,**kwargs):
		if kwargs.has_key('instants') and kwargs.has_key('persists') and kwargs.has_key('pactivates') and kwargs.has_key('elemental'):
			self.instants = kwargs['instants']
			self.persists = kwargs['persists']
			self.pactivates = kwargs['pactivates']
			self.elementals = list(kwargs['elemental'])
		elif kwargs.has_key('element'):
			element = kwargs['element']
			self.instants = Instant_List(element=parse_element(element,'instants'))
			self.persists = Persist_Cond_list(element=parse_element(element,'persists'))
			self.pactivates = Persist_Activate_list(element=parse_element(element,'pactivates'))
			self.elementals = []
			for element in parse_elements(element,'elementals'):
				self.elementals.append(parse_string(element,'elemental'))
		else:
			raise PP_Game_Action_Error("Card Effect instantiated with improper constructor%s"%str(kwargs.keys()))

	def on_activate(self,game,uid):
		self.instants(game,uid)

	def account_for(self,game,uid,action):
		self.pactivates.account_for(game,uid)

	def does_persist(self,game,uid):
		self.persists(game,uid)

	def xml_output(self,full):
		xml = ''
		xml += '<instants>%s</instants>'%self.instants.xml_output(full)
		xml += '<persists>%s</persists>'%self.persists.xml_output(full)
		xml += '<pactivates>%s</pactivates>'%self.pactivates.xml_output(full)
		xml += '<elementals>'
		for elemental in self.elementals:
			xml += '<elemental>%s</elemental>'%str(elemental)
		xml += '</elementals>'
		return xml
