from src.control.gameHandle.card.effects import DirectDamage
from src.control.gameHandle.card.conds import Valid
from src.control.gameHandle.card.lookups.Lookups import InstantLookUp

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
		if effect == None:
			self.effect = None
		else:
			self.effect = effect
		if conds == None
			self.conds = []
		else:
			self.conds = conds

	def setEffect(self,effect):
		self.effect = effect

	def addCond(self,cond):
		self.conds.append(cond)

	def isValid(self,game):
		valid = True
		for cond in self.conds:
			valid = valid and cond.isValid(game)
		return valid

	def applyTo(self,action,game):
		if self.isValid(game):
			self.effect.applyTo(action,game)

class DummyInstantList:
	def isValid(self,game):
		return False

	def applyTo(self,action,game):
		pass
