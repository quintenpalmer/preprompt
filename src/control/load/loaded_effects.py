from src.control.game_logic.card_effect.elements import get_element_from_string
from src.control.game_logic.card_effect.instant import Instant_List
from src.control.game_logic.card_effect.instant import Instant
from src.control.game_logic.card_effect.persist import Persist_Cond_list
from src.control.game_logic.card_effect.persist_activate import Persist_Activate
from src.control.game_logic.card_effect.persist_activate import Persist_Activate_list
from src.control.game_logic.card_effect.effect import Effect

def get_direct_damage(element,amount):
	instants = Instant_List()
	instant = Instant()
	instant.set_effect(Direct_Damage(element,amount))
	instant.add_cond(Valid_Activate())
	instants.add_instant(instant)

	persists = Persist_Cond_list()
	persists.add_cond(In_Valid_persist())

	pactivates = Persist_Activate_list()
	pactivate = Persist_Activate()
	pactivate.add_cond(Valid_Activate())
	pactivate.set_effect(Do_Nothing())

	return Effect(instants,persists,pactivates,element)

def get_sits_nTurns(element,amount):
	instants = Instant_List()
	instant = Instant()
	instant.set_effect(Do_Nothing())
	instant.add_cond(Valid_Activate())
	instants.add_instant(instant)

	persists = Persist_Cond_list()
	persists.add_cond(Timed_Persist(amount))

	pactivates = Persist_Activate_list()
	pactivate = Persist_Activate()
	pactivate.add_cond(Valid_Activate())
	pactivate.set_effect(Do_Nothing())
	pactivates.add_trigger(pactivate)

	return Effect(instants,persists,pactivates,element)

class Timed_Persist:
	def __init__(self,amount):
		self.current_turns = amount
		self.start_turns = amount
	def tick(self,game,uid):
		self.current_turns -= 1
	def persists(self,game,uid):
		return self.turns >= 0
	def reset(self,game,uid):
		self.current_turns = self.start_turns

class Direct_Damage:
	def __init__(self,element,amount):
		self.element = get_element_from_string(element)
		self.amount = int(amount)

	def apply_to(self,action):
		action.element = self.element
		action.damage = self.amount

class Valid_Activate:
	def is_valid(self,action,game,uid):
		return True

class In_Valid_persist:
	def tick(self,game,uid):
		pass
	def persists(self,game,uid):
		return False
	def reset(self,game,uid):
		pass

class Do_Nothing:
	def apply_to(self,action):
		pass
