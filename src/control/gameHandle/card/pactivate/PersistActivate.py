
class PersistActivateList:
	def __init__(self):
		self.persistActivates = []

	def onAct(self,action,game,uid):
		for pactivate in self.persistActivates:
			pactivate.onAct(action,game,uid)

class DummyPersistActivateList:
	def onAct(self,action,game,uid):
		pass
