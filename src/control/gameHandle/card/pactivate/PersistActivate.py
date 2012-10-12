
class PersistActivateList:
	def __init__(self):
		self.persistActivates = []

	def onAct(self,action,game,uid):
		for pactivate in self.persistActivates:
			pactivate.onAct(action,game,uid)

class PersistActivate:
	def __init__(self,effect=None,conds=None):
		self.effect = effect
		if conds == None:
			self.conds = []
		else:
			self.conds = conds

	def onAct(self,action,game,uid):	
		if self.isValid(action,game,uid):
			self.effect.applyTo(action,game)

	def isValid(self,action,game,uid):
		valid = True
		for cond in self.conds:
			valid = valid and cond.isValid(action,game,uid)
		return valid
	
	def addEffect(self,effect):
		self.effect = effect

	def addCond(self,cond):
		self.conds.append(cond)

class DummyPersistActivateList:
	def onAct(self,action,game,uid):
		pass
