from src.control.gameHandle.card.elements import getElementFromString
from src.control.gameHandle.card.instant.Instant import InstantList
from src.control.gameHandle.card.instant.Instant import Instant
from src.control.gameHandle.card.persist.Persist import PersistCondList
from src.control.gameHandle.card.pactivate.PersistActivate import PersistActivate
from src.control.gameHandle.card.pactivate.PersistActivate import PersistActivateList
from src.control.gameHandle.card.Effect import Effect

def getDirectDamage(element,amount):
	instants = InstantList()
	instant = Instant()
	instant.setEffect(DirectDamage(element,amount))
	instant.addCond(ValidActivate())
	instants.addInstant(instant)

	persists = PersistCondList()
	persists.addCond(InValidPersist())

	pactivates = PersistActivateList()
	pactivate = PersistActivate()
	pactivate.addCond(ValidActivate())
	pactivate.setEffect(DoNothing())
	
	return Effect(instants,persists,pactivates,element)

def getSitsNTurns(element,amount):
	instants = InstantList()
	instant = Instant()
	instant.setEffect(DoNothing())
	instant.addCond(ValidActivate())
	instants.addInstant(instant)

	persists = PersistCondList()
	persists.addCond(TimedPersist(amount))

	pactivates = PersistActivateList()
	pactivate = PersistActivate()
	pactivate.addCond(ValidActivate())
	pactivate.setEffect(DoNothing())
	pactivates.addTrigger(pactivate)

	return Effect(instants,persists,pactivates,element)

class TimedPersist:
	def __init__(self,amount):
		self.currentTurns = amount
		self.startTurns = amount
	def tick(self,game,uid):
		self.currentTurns -= 1
	def persists(self,game,uid):
		return self.turns >= 0
	def reset(self,game,uid):
		self.currentTurns = self.startTurns

class DirectDamage:
	def __init__(self,element,amount):
		self.element = getElementFromString(element)
		self.amount = int(amount)

	def applyTo(self,action):
		action.element = self.element
		action.damage = self.amount

class ValidActivate:
	def isValid(self,action,game,uid):
		return True

class InValidPersist:
	def tick(self,game,uid):
		pass
	def persists(self,game,uid):
		return False
	def reset(self,game,uid):
		pass

class DoNothing:
	def applyTo(self,action):
		pass

def getInstant(lookup):
	print lookup
	instant = InstantList()
	for look in lookup:
		lookup = lookup.split(',')
		print lookup
		try:
			instant.instants.append(InstantLookUp[lookup])
		except KeyError:
			return DummyInstant()
			#return DirectDamage(lookup[2],lookup[3])
