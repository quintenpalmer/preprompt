from src.control.gameHandle.card.instant.Instant import InstantList
from src.control.gameHandle.card.persist.Persist import PersistList
from src.control.gameHandle.card.pactivate.PersistActivate import PersistActivateList

class Effect:
	def __init__(self):
		self.instants = InstantList()
		self.persists = PersistList()
		self.pactivates = PersistActivateList()

	def onActivate(self,game,uid):
		self.instants(game,uid)

	def accountFor(self,game,uid,action):
		self.pactivates.accountFor(game,uid)

	def doesPersist(self,game,uid):
		self.persists(game,uid)
