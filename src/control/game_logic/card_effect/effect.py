from src.control.game_logic.card_effect.instant import Instant_List
from src.control.game_logic.card_effect.persist import Persist_Cond_list
from src.control.game_logic.card_effect.persist_activate import Persist_Activate_list

class Effect:
	def __init__(self,instants,persists,pactivates,elements):
		self.instants = instants
		self.persists = persists
		self.pactivates = pactivates
		if type(elements) is list:
			self.elements = list(elements)
		else:
			self.elements = [elements]

	def on_activate(self,game,uid):
		self.instants(game,uid)

	def account_for(self,game,uid,action):
		self.pactivates.account_for(game,uid)

	def does_persist(self,game,uid):
		self.persists(game,uid)
