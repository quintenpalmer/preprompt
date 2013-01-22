from src.control.game_logic.card_effect.elements import getElementFromString

class DirectDamage:
	def __init__(self,element,amount):
		self.element = getElementFromString(element)
		self.amount = int(amount)

	def applyTo(self,action):
		action.element = self.element
		action.damage = self.amount
