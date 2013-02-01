from src.control.card_effect.elements import get_element_from_string
from src.control.card_effect.instant import Instant_List
from src.control.card_effect.instant import Instant
from src.control.card_effect.persist import Persist_Cond_list
from src.control.card_effect.persist_activate import Persist_Activate
from src.control.card_effect.persist_activate import Persist_Activate_list
from src.control.card_effect.effect import Effect
from src.control.card_effect.abstract_effects import Abstract_Instant_Effect, Abstract_Instant_Cond, Abstract_Persist_Cond, Abstract_Trigger_Effect, Abstract_Trigger_Cond
from src.model.control_state import phase

from src.model.card import Card

def get_direct_damage(element,amount):
	instants = Instant_List(Instant(Direct_Damage(element,amount),Valid_Activate()),phase.main)
	persists = Persist_Cond_list(False,In_Valid_persist())
	pactivates = Persist_Activate_list(Persist_Activate(Do_Nothing_Trigger(),Valid_Trigger_Cond()))
	return Effect(instants,persists,pactivates,element)

def get_sits_n_turns(element,duration):
	instants = Instant_List(Instant(Do_Nothing(),Valid_Activate()),phase.main)
	persists = Persist_Cond_list(True,Timed_Persist(duration))
	pactivates = Persist_Activate_list(Persist_Activate(Do_Nothing_Trigger(),Valid_Trigger_Cond()))
	return Effect(instants,persists,pactivates,element)

def alters_m_sits_n_turns(element,args):
	tmp = args.split('/')
	duration = tmp[0]
	amount = tmp[1]
	who = [int(t) for t in tmp[2]]
	instants = Instant_List(Instant(Do_Nothing(),Valid_Activate()),phase.main)
	persists = Persist_Cond_list(True,Timed_Persist(duration))
	pactivates = Persist_Activate_list(Persist_Activate(Add_Damage(element,amount),On_Damager(who)))
	return Effect(instants,persists,pactivates,element)

def lookup_table(lookup_string):
	tmp = lookup_string.split('-')
	element_type = tmp[0]
	effect_type = tmp[1]
	params = tmp[2]
	return Card(tmp[1],ntoe[effect_type](element_type,params))

# name to effect mapping
ntoe = {}
ntoe['damage'] = get_direct_damage
ntoe['persists'] = get_sits_n_turns
ntoe['alter'] = alters_m_sits_n_turns

class Timed_Persist(Abstract_Persist_Cond):
	def __init__(self,amount):
		self.current_turns = amount
		self.start_turns = amount
	def tick(self,action):
		self.current_turns -= 1
	def persists(self,action):
		return self.turns >= 0
	def reset(self,action):
		self.current_turns = self.start_turns

class Direct_Damage(Abstract_Instant_Effect):
	def __init__(self,element,amount):
		self.element = get_element_from_string(element)
		self.amount = int(amount)

	def apply_to(self,action):
		action.element = self.element
		action.damage = self.amount

class Add_Damage(Abstract_Trigger_Effect):
	def __init__(self,element,amount):
		self.element = get_element_from_string(element)
		self.amount = int(amount)

	def apply_to(self,action):
		action.damage += self.amount

class On_Damager(Abstract_Trigger_Cond):
	def __init__(self,who):
		self.who = who

	def is_valid(self,action,card_owner):
		if action.base_damage > 0:
			if card_owner in self.who:
				return True
		return False

class Valid_Trigger_Cond(Abstract_Trigger_Cond):
	def is_valid(self,action,card_owner):
		return True
		

class Valid_Activate(Abstract_Instant_Cond):
	def is_valid(self,action):
		return True

class In_Valid_persist(Abstract_Persist_Cond):
	def tick(self,action):
		pass
	def persists(self,action):
		return False
	def reset(self,action):
		pass

class Do_Nothing_Trigger(Abstract_Trigger_Effect):
	def apply_to(self,action):
		pass

class Do_Nothing(Abstract_Instant_Effect):
	def apply_to(self,action):
		pass

