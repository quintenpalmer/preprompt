from src.control.gameHandle.card.instants.Instant import InstantList

class Effect:
	def __init__(self):
		self.instants = InstantList()
		self.persists = PersistList()
		self.pactivates = PersistActivateList()
