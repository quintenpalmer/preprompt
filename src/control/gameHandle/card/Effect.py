from src.control.gameHandle.card.instants.Instant import InstantList

class Effect:
	def __init__(self):
		self.instants = InstantList()
		self.persists = PersistList()
		self.pactivates = PersistActivateList()

	def accountFor(self,game,uid,action):
		self.pactivates.accountFor(game,uid)

	def onActivate(self,game,uid):
		self.instants(game,uid)

	def doesPersist(self,game,uid):
		self.persists(game,uid)
