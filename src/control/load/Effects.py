from src.control.game_logic.card_effect.elements import getElement_FromString
from src.control.game_logic.card_effect.instant.Instant import Instant_List
from src.control.game_logic.card_effect.instant.Instant import Instant
from src.control.game_logic.card_effect.persist.Persist import Persist_CondList
from src.control.game_logic.card_effect.pactivate.Persist_Activate import Persist_Activate
from src.control.game_logic.card_effect.pactivate.Persist_Activate import Persist_ActivateList
from src.control.game_logic.card_effect.Effect import Effect

def getDirect_Damage(element,amount):
	instants = Instant_List()
	instant = Instant()
	instant.setEffect(Direct_Damage(element,amount))
	instant.addCond(Valid_Activate())
	instants.addInstant(instant)

	persists = Persist_CondList()
	persists.addCond(In_ValidPersist())

	pactivates = Persist_ActivateList()
	pactivate = Persist_Activate()
	pactivate.addCond(Valid_Activate())
	pactivate.setEffect(Do_Nothing())
	
	return Effect(instants,persists,pactivates,element)

def getSits_NTurns(element,amount):
	instants = Instant_List()
	instant = Instant()
	instant.setEffect(Do_Nothing())
	instant.addCond(Valid_Activate())
	instants.addInstant(instant)

	persists = Persist_CondList()
	persists.addCond(Timed_Persist(amount))

	pactivates = Persist_ActivateList()
	pactivate = Persist_Activate()
	pactivate.addCond(Valid_Activate())
	pactivate.setEffect(Do_Nothing())
	pactivates.addTrigger(pactivate)

	return Effect(instants,persists,pactivates,element)

class Timed_Persist:
	def __init__(self,amount):
		self.currentTurns = amount
		self.startTurns = amount
	def tick(self,game,uid):
		self.currentTurns -= 1
	def persists(self,game,uid):
		return self.turns >= 0
	def reset(self,game,uid):
		self.currentTurns = self.startTurns

class Direct_Damage:
	def __init__(self,element,amount):
		self.element = getElement_FromString(element)
		self.amount = int(amount)

	def applyTo(self,action):
		action.element = self.element
		action.damage = self.amount

class Valid_Activate:
	def isValid(self,action,game,uid):
		return True

class In_ValidPersist:
	def tick(self,game,uid):
		pass
	def persists(self,game,uid):
		return False
	def reset(self,game,uid):
		pass

class Do_Nothing:
	def applyTo(self,action):
		pass

def getInstant(lookup):
	print lookup
	instant = Instant_List()
	for look in lookup:
		lookup = lookup.split(',')
		print lookup
		try:
			instant.instants.append(Instant_LookUp[lookup])
		except Key_Error:
			return Dummy_Instant()
			#return Direct_Damage(lookup[2],lookup[3])
