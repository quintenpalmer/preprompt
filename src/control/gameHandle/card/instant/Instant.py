from src.control.gameHandle.card.effects import DirectDamage
from src.control.gameHandle.card.conds import Valid

class InstantList:
	def __init__(self):
		self.instants = []

	def addInstant(self,instant):
		self.instants.append(instant)

	def applyTo(self,action,game):
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

	def isValid(self,action,game,uid):
		valid = True
		for cond in self.conds:
			valid = valid and cond.isValid(action,game,uid)
		return valid

	def applyTo(self,action,game):
		if self.isValid(action,game,uid):
			self.effect.applyTo(action,game,uid)

class DummyInstantList:
	def isValid(self,game):
		return False

	def applyTo(self,action,game):
		pass
