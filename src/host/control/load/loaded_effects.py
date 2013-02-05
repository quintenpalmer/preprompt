from model.card_effect.elementals import get_elemental_from_string
from model.card_effect.instant import Instant_List, Instant
from model.card_effect.persist import Persist_Cond_list
from model.card_effect.persist_activate import Persist_Activate_list,Persist_Activate
from model.card_effect.effect import Effect
from model.card_effect.abstract_effects import Abstract_Instant_Effect, Abstract_Instant_Cond, Abstract_Persist_Cond, Abstract_Trigger_Effect, Abstract_Trigger_Cond
from model.control_state import phase

from pyplib.xml_parser import parse_int
from model.errors import Game_Action_Error

from model.card import Card

def get_direct_damage(elemental,amount):
	instants = Instant_List(instants=[Instant(effect=Direct_Damage(elemental=elemental,amount=amount),conds=[Valid_Activate()])],valid_phase=phase.main)
	persists = Persist_Cond_list(does_persist=False,conds=[In_Valid_persist()])
	pactivates = Persist_Activate_list(pactivates=[Persist_Activate(effect=Do_Nothing_Trigger(),conds=[Valid_Trigger_Cond()])])
	return Effect(instants=instants,persists=persists,pactivates=pactivates,elemental=elemental)

def get_sits_n_turns(elemental,duration):
	instants = Instant_List(instants=[Instant(effect=Do_Nothing(),conds=[Valid_Activate()])],valid_phase=phase.main)
	persists = Persist_Cond_list(does_persist=True,conds=[Timed_Persist(duration=duration)])
	pactivates = Persist_Activate_list(pactivates=[Persist_Activate(effect=Do_Nothing_Trigger(),conds=[Valid_Trigger_Cond()])])
	return Effect(instants=instants,persists=persists,pactivates=pactivates,elemental=elemental)

def alters_m_sits_n_turns(elemental,args):
	tmp = args.split('/')
	duration = int(tmp[0])
	amount = int(tmp[1])
	who = [int(t) for t in tmp[2]]
	instants = Instant_List(instants=[Instant(effect=Do_Nothing(),conds=[Valid_Activate()])],valid_phase=phase.main)
	persists = Persist_Cond_list(does_persist=True,conds=[Timed_Persist(duration=duration)])
	pactivates = Persist_Activate_list(pactivates=[Persist_Activate(effect=Add_Damage(elemental=elemental,amount=amount),conds=[On_Damager(who=who)])])
	return Effect(instants=instants,persists=persists,pactivates=pactivates,elemental=elemental)

def lookup_table(lookup_string):
	tmp = lookup_string.split('-')
	elemental_type = tmp[0]
	effect_type = tmp[1]
	params = tmp[2]
	return Card(name=tmp[1],effect=ntoe[effect_type](elemental_type,params))

class Direct_Damage(Abstract_Instant_Effect):
	def __init__(self,**kwargs):
		if kwargs.has_key('elemental') and kwargs.has_key('amount'):
			self.elemental = get_elemental_from_string(kwargs['elemental'])
			self.amount = int(kwargs['amount'])
		elif kwargs.has_key('element'):
			element = kwargs['element']
		else:
			raise Game_Action_Error('Direct_Damage instantiated with invalid constructor %s'%kwargs.keys())

	def apply_to(self,action):
		action.elemental = self.elemental
		action.damage = self.amount

	def xml_output(self):
		xml = '<name>Direct_Damage</name>'
		xml += '<elemental>%s</elemental>'%str(self.elemental)
		xml += '<amount>%s</amount>'%str(self.amount)
		return xml

class Do_Nothing(Abstract_Instant_Effect):
	def apply_to(self,action):
		pass
	def xml_output(self):
		return '<name>Do_Nothing</name>'

class Valid_Activate(Abstract_Instant_Cond):
	def is_valid(self,action):
		return True
	def xml_output(self):
		return '<name>Valid_Activate</name>'

class Timed_Persist(Abstract_Persist_Cond):
	def __init__(self,**kwargs):
		if kwargs.has_key('duration'):
			self.current_turns = kwargs['duration']
			self.start_turns = kwargs['duration']
		elif kwargs.has_key('element'):
			element = kwargs['element']
			self.current_turns = parse_int(element,'current_turns')
			self.start_turns = parse_int(element,'start_turns')
		else:
			raise Game_Action_Error('Timed_Persist instantiated with invalid constructor %s'%kwargs.keys())
	def tick(self,action):
		self.current_turns -= 1
	def persists(self,action):
		return self.turns >= 0
	def reset(self,action):
		self.current_turns = self.start_turns
	def xml_output(self):
		xml = '<name>Timed_Persist</name>'
		xml += '<current_turns>%s</current_turns>'%str(self.current_turns)
		xml += '<start_turns>%s</start_turns>'%str(self.start_turns)
		return xml

class In_Valid_persist(Abstract_Persist_Cond):
	def tick(self,action):
		pass
	def persists(self,action):
		return False
	def reset(self,action):
		pass
	def xml_output(self):
		return '<name>Invalid_Persist</name>'

class Add_Damage(Abstract_Trigger_Effect):
	def __init__(self,**kwargs):
		if kwargs.has_key('elemental') and kwargs.has_key('amount'):
			self.elemental = get_elemental_from_string(kwargs['elemental'])
			self.amount = int(kwargs['amount'])
		elif kwargs.has_key('element'):
			element = kwargs['element']
			self.elemental = parse_int(element,'elemental')
			self.amount = parse_int(element,'amount')
		else:
			raise Game_Action_Error('Add_Damage instantiated with invalid constructor %s'%kwargs.keys())

	def apply_to(self,action):
		action.damage += self.amount

	def xml_output(self):
		xml = '<name>Add_Damage</name>'
		xml += '<elemental>%s</elemental>'%str(self.elemental)
		xml += '<amount>%s</amount>'%str(self.amount)
		return xml

class Do_Nothing_Trigger(Abstract_Trigger_Effect):
	def apply_to(self,action):
		pass
	def xml_output(self):
		return '<name>Do_Nothing_Trigger</name>'

class Valid_Trigger_Cond(Abstract_Trigger_Cond):
	def is_valid(self,action,card_owner):
		return True
	def xml_output(self):
		return '<name>Valid_Trigger_Cond</name>'

class On_Damager(Abstract_Trigger_Cond):
	def __init__(self,**kwargs):
		if kwargs.has_key('who'):
			self.who = kwargs['who']
		elif kwargs.has_key('element'):
			element = kwargs['element']
			self.who = parse_int(element,'who')
		else:
			raise Game_Action_Error('On_Damager instantiated with invalid constructor %s'%kwargs.keys())

	def is_valid(self,action,card_owner):
		if action.base_damage > 0:
			if card_owner in self.who:
				return True
		return False

	def xml_output(self):
		xml = '<name>On_Damager</name>'
		xml += '<who>%s</who>'%str(self.who)
		return xml

# name to effect mapping
ntoe = {}
ntoe['damage'] = get_direct_damage
ntoe['persists'] = get_sits_n_turns
ntoe['alter'] = alters_m_sits_n_turns

xntoe = {}
xntoe['Direct_Damage'] = Direct_Damage
xntoe['Do_Nothing'] = Do_Nothing
xntoe['Valid_Activate'] = Valid_Activate
xntoe['Timed_Persist'] = Timed_Persist
xntoe['In_Valid_persist'] = In_Valid_persist
xntoe['Add_Damage'] = Add_Damage
xntoe['Valid_Trigger_Cond'] = Valid_Trigger_Cond
xntoe['On_Damager'] = On_Damager

