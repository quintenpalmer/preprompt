
class Persist_Activate_list:
	def __init__(self,pactivate):
		if type(pactivate) == list:
			self.persist_activates = pactivate
		else:
			self.persist_activates = [pactivate]

	def add_trigger(self,pactivate):
		self.persist_activates.append(pactivate)

	def on_act(self,action):
		for pactivate in self.persist_activates:
			pactivate.on_act(action)

class Persist_Activate:
	def __init__(self,effect,conds):
		self.effect = effect
		if type(conds) == list:
			self.conds = conds
		else:
			self.conds = [conds]

	def on_act(self,action):
		if self.is_valid(action):
			self.effect.apply_to(action)

	def is_valid(self,action):
		valid = True
		for cond in self.conds:
			valid = valid and cond.is_valid(action)
		return valid

	def set_effect(self,effect):
		self.effect = effect

	def add_cond(self,cond):
		self.conds.append(cond)

class Dummy_Persist_activate_list:
	def on_act(self,action):
		pass
