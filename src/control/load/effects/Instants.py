from src.control.game_logic.card_effect.elements import getElement_FromString
from src.control.game_logic.card_effect.instant.Instant import Instant_List
from src.control.game_logic.card_effect.instant.Instant import Instant

class Direct_Damage:
	def __init__(self,element,amount):
		self.element = getElement_FromString(element)
		self.amount = int(amount)

	def applyTo(self,action):
		action.element = self.element
		action.damage = self.amount

def getDirect_Damage(element,amount):
	iList = Instant_List()
	instant = Instant()
	instant.setEffect(Direct_Damage(element,amount))
	instant.addCond(Valid())
	iList.addInstant(instant)
	return iList

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

class Valid:
	def isValid(self,action,game,uid):
		return True
