
class PersistCondList:
	def __init__(self):
		self.conds = []

	def tick(self,game,uid):
		for cond in self.conds:
			cond.tick(game,uid)

	def persists(self,game,uid):
		doesPersist = True
		for cond in self.conds:
			doesPersist = doesPersist and cond.persists
		return doesPersist

	def reset(self,game,uid):
		for cond in self.conds:
			cond.reset(game,uid)

	def addPersistCond(self,pcond):
		self.conds.append(pcond)

class DummyPersistCondList:
	def tick(self,game,uid):
		pass
	def persists(self,game,uid):
		return True
	def reset(self,game,uid):
		pass
