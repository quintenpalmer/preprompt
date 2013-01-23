
class Persist_ActivateList:
	def __init__(self):
		self.persistActivates = []

	def addTrigger(self,pactivate):
		self.persistActivates.append(pactivate)

	def onAct(self,action,game,uid):
		for pactivate in self.persistActivates:
			pactivate.onAct(action,game,uid)

class Persist_Activate:
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
	
	def setEffect(self,effect):
		self.effect = effect

	def addCond(self,cond):
		self.conds.append(cond)

class Dummy_PersistActivate_List:
	def onAct(self,action,game,uid):
		pass
