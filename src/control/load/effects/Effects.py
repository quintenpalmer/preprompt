from src.control.game_logic.card_effect.elements import getElement_FromString

class Direct_Damage:
	def __init__(self,element,amount):
		self.element = getElement_FromString(element)
		self.amount = int(amount)

	def applyTo(self,action):
		action.element = self.element
		action.damage = self.amount
