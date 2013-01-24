from src.control.game_logic.card_effect.elements import get_element_from_string
from src.control.game_logic.card_effect.instant import Instant_List
from src.control.game_logic.card_effect.instant import Instant
from src.control.game_logic.card_effect.persist import Persist_Cond_list
from src.control.game_logic.card_effect.persist_activate import Persist_Activate
from src.control.game_logic.card_effect.persist_activate import Persist_Activate_list
from src.control.game_logic.card_effect.effect import Effect
from src.model.phase import phase
from src.control.game_logic.card_effect.effect_types import Abstract_Instant_Effect, Abstract_Instant_Cond
from src.control.game_logic.card_effect.effect_types import Abstract_Persist_Cond

def get_direct_damage(element,amount):
	instants = Instant_List(Instant(Direct_Damage(element,amount),Valid_Activate()),phase.main)
	persists = Persist_Cond_list(In_Valid_persist())
	pactivates = Persist_Activate_list(Persist_Activate(Do_Nothing(),Valid_Activate()))
	return Effect(instants,persists,pactivates,element)

def get_sits_nTurns(element,amount):
	instants = Instant_List(Instant(Do_Nothing(),Valid_Activate()),phase.main)
	persists = Persist_Cond_list([Timed_Persist(amount)])
	pactivates = Persist_Activate_list(Persist_Activate(Do_Nothing(),[Valid_Activate()]))
	return Effect(instants,persists,pactivates,element)

class Timed_Persist(Abstract_Persist_Cond):
	def __init__(self,amount):
		self.current_turns = amount
		self.start_turns = amount
	def tick(self,game,uid):
		self.current_turns -= 1
	def persists(self,game,uid):
		return self.turns >= 0
	def reset(self,game,uid):
		self.current_turns = self.start_turns

class Direct_Damage(Abstract_Instant_Effect):
	def __init__(self,element,amount):
		self.element = get_element_from_string(element)
		self.amount = int(amount)

	def apply_to(self,action):
		action.element = self.element
		action.damage = self.amount

class Valid_Activate(Abstract_Instant_Cond):
	def is_valid(self,action,game,uid):
		return True

class In_Valid_persist(Abstract_Persist_Cond):
	def tick(self,game,uid):
		pass
	def persists(self,game,uid):
		return False
	def reset(self,game,uid):
		pass

class Do_Nothing(Abstract_Instant_Effect):
	def apply_to(self,action):
		pass
