from src.model.clist import cltypes

class PlayArgs:
	def __init__(self,game,srcUid,srcCard,srcList,tgtUid,tgtCard,tgtList):
		self.game = game
		self.srcUid = srcUid
		self.srcCard = srcCard
		self.srcList = srcList

		self.tgtUid = tgtUid
		self.tgtCard = tgtCard
		self.tgtList = tgtList
