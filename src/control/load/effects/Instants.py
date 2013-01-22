from src.control.game_logic.card_effect.elements import getElementFromString
from src.control.game_logic.card_effect.instant.Instant import InstantList
from src.control.game_logic.card_effect.instant.Instant import Instant

class DirectDamage:
	def __init__(self,element,amount):
		self.element = getElementFromString(element)
		self.amount = int(amount)

	def applyTo(self,action):
		action.element = self.element
		action.damage = self.amount

def getDirectDamage(element,amount):
	iList = InstantList()
	instant = Instant()
	instant.setEffect(DirectDamage(element,amount))
	instant.addCond(Valid())
	iList.addInstant(instant)
	return iList

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

class Valid:
	def isValid(self,action,game,uid):
		return True
