
class Instant_List:
	def __init__(self):
		self.instants = []

	def addInstant(self,instant):
		self.instants.append(instant)

	def applyTo(self,action):
		for instant in self.instants:
			instant.applyTo(action)

class Instant:
	def __init__(self,effect=None,conds=None):
		self.effect = effect
		if conds == None:
			self.conds = []
		else:
			self.conds = conds

	def setEffect(self,effect):
		self.effect = effect

	def addCond(self,cond):
		self.conds.append(cond)

	def isValid(self,action):
		valid = True
		for cond in self.conds:
			valid = valid and cond.isValid(action,action.game,action.me.player.uid)
		return valid

	def applyTo(self,action):
		if self.isValid(action):
			self.effect.applyTo(action)

class Dummy_InstantList:
	def isValid(self,game):
		return False

	def applyTo(self,action,game):
		pass
