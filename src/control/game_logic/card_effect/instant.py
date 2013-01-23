
class Instant_List:
	def __init__(self):
		self.instants = []

	def add_instant(self,instant):
		self.instants.append(instant)

	def apply_to(self,action):
		for instant in self.instants:
			instant.apply_to(action)

class Instant:
	def __init__(self,effect=None,conds=None):
		self.effect = effect
		if conds == None:
			self.conds = []
		else:
			self.conds = conds

	def set_effect(self,effect):
		self.effect = effect

	def add_cond(self,cond):
		self.conds.append(cond)

	def is_valid(self,action):
		valid = True
		for cond in self.conds:
			valid = valid and cond.is_valid(action,action.game,action.me.player.uid)
		return valid

	def apply_to(self,action):
		if self.is_valid(action):
			self.effect.apply_to(action)

class Dummy_Instant_list:
	def is_valid(self,game):
		return False

	def apply_to(self,action,game):
		pass
