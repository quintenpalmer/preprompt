
class Persist_Cond_list:
	def __init__(self):
		self.conds = []

	def tick(self,game,uid):
		for cond in self.conds:
			cond.tick(game,uid)

	def persists(self,game,uid):
		does_persist = True
		for cond in self.conds:
			does_persist = does_persist and cond.persists
		return does_persist

	def reset(self,game,uid):
		for cond in self.conds:
			cond.reset(game,uid)

	def add_cond(self,pcond):
		self.conds.append(pcond)

class Dummy_Persist_cond_list:
	def tick(self,game,uid):
		pass
	def persists(self,game,uid):
		return True
	def reset(self,game,uid):
		pass
