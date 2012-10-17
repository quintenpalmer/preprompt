from src.control.gameHandle.card.elements import getElementFromString

class DirectDamage:
	def __init__(self,element,amount):
		self.element = getElementFromString(element)
		self.amount = int(amount)

	def applyTo(self,action):
		action.element = self.element
		action.damage = self.amount

def getInstant(lookup):
	iList = InstantList()
	instant = Instant()
	instant.setEffect(DirectDamage('f',3))
	instant.addCond(Valid())
	iList.addInstant(instant)
	return iList
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
	def isValid(self,game,uid):
		return True
