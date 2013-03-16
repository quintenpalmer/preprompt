from pyplib.xml_parser import parse_int,parse_elements
from pyplib.errors import PP_Game_Action_Error

from model.card_effect.abstract_effects import Abstract_Instant_Effect, Abstract_Instant_Cond, Abstract_Persist_Cond, Abstract_Trigger_Effect, Abstract_Trigger_Cond
from model.card_effect.elementals import get_elemental_from_string

class Config_Args:
	def __init__(self,config_player1,config_player2):
		self.config_player1 = config_player1
		self.config_player2 = config_player2

class Config_Player:
	def __init__(self,uid,did):
		self.uid = uid
		self.did = did

class Direct_Damage(Abstract_Instant_Effect):
	def __init__(self,**kwargs):
		if kwargs.has_key('elemental') and kwargs.has_key('amount'):
			self.elemental = get_elemental_from_string(kwargs['elemental'])
			self.amount = int(kwargs['amount'])
		elif kwargs.has_key('element'):
			element = kwargs['element']
			self.elemental = parse_int(element,'elemental')
			self.amount = parse_int(element,'amount')
		else:
			raise PP_Game_Action_Error('Direct_Damage instantiated with invalid constructor %s'%kwargs.keys())

	def apply_to(self,action):
		action.elemental = self.elemental
		action.damage = self.amount

	def xml_output(self):
		xml = '<name>Direct_Damage</name>'
		xml += '<elemental>%s</elemental>'%str(self.elemental)
		xml += '<amount>%s</amount>'%str(self.amount)
		return xml

class Do_Nothing(Abstract_Instant_Effect):
	def __init__(self,**kwargs):
		if len(kwargs) == 0:
			pass
		elif kwargs.has_key('element'):
			pass
		else:
			raise PP_Game_Action_Error('Do_Nothing instantiated with invalid constructor %s'%kwargs.keys())
	def apply_to(self,action):
		pass
	def xml_output(self):
		return '<name>Do_Nothing</name>'

class Valid_Activate(Abstract_Instant_Cond):
	def __init__(self,**kwargs):
		if len(kwargs) == 0:
			pass
		elif kwargs.has_key('element'):
			pass
		else:
			raise PP_Game_Action_Error('Do_Nothing instantiated with invalid constructor %s'%kwargs.keys())
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
			raise PP_Game_Action_Error('Timed_Persist instantiated with invalid constructor %s'%kwargs.keys())
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
	def __init__(self,**kwargs):
		if len(kwargs) == 0:
			pass
		elif kwargs.has_key('element'):
			pass
		else:
			raise PP_Game_Action_Error('Do_Nothing instantiated with invalid constructor %s'%kwargs.keys())
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
			raise PP_Game_Action_Error('Add_Damage instantiated with invalid constructor %s'%kwargs.keys())

	def apply_to(self,action):
		action.damage += self.amount

	def xml_output(self):
		xml = '<name>Add_Damage</name>'
		xml += '<elemental>%s</elemental>'%str(self.elemental)
		xml += '<amount>%s</amount>'%str(self.amount)
		return xml

class Do_Nothing_Trigger(Abstract_Trigger_Effect):
	def __init__(self,**kwargs):
		if len(kwargs) == 0:
			pass
		elif kwargs.has_key('element'):
			pass
		else:
			raise PP_Game_Action_Error('Do_Nothing instantiated with invalid constructor %s'%kwargs.keys())
	def apply_to(self,action):
		pass
	def xml_output(self):
		return '<name>Do_Nothing_Trigger</name>'

class Valid_Trigger_Cond(Abstract_Trigger_Cond):
	def __init__(self,**kwargs):
		if len(kwargs) == 0:
			pass
		elif kwargs.has_key('element'):
			pass
		else:
			raise PP_Game_Action_Error('Do_Nothing instantiated with invalid constructor %s'%kwargs.keys())
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
			self.who = []
			for who in parse_elements(element,'who'):
				self.who.append(parse_int(element,'who'))
		else:
			raise PP_Game_Action_Error('On_Damager instantiated with invalid constructor %s'%kwargs.keys())

	def is_valid(self,action,card_owner):
		if action.base_damage > 0:
			if card_owner in self.who:
				return True
		return False

	def xml_output(self):
		xml = '<name>On_Damager</name>'
		for w in self.who:
			xml += '<who>%s</who>'%str(w)
		return xml

xntoe = {}
xntoe['Direct_Damage'] = Direct_Damage
xntoe['Do_Nothing'] = Do_Nothing
xntoe['Valid_Activate'] = Valid_Activate
xntoe['Timed_Persist'] = Timed_Persist
xntoe['Invalid_Persist'] = In_Valid_persist
xntoe['Add_Damage'] = Add_Damage
xntoe['Valid_Trigger_Cond'] = Valid_Trigger_Cond
xntoe['On_Damager'] = On_Damager
xntoe['Do_Nothing_Trigger'] = Do_Nothing_Trigger

def get_effect_from_xml_name(xml_name):
	try:
		return xntoe[xml_name]
	except KeyError:
		raise PP_Game_Action_Error("Could not load effect from the xml tag %s"%str(xml_name))
