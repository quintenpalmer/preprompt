from src.model.clist import cltypes

class PlayArgs:
	def __init__(self,game,uid,targetCard,targetList=None):
		player = game.getMeFromUid(uid)
		self.targetCard = targetCard
		clist = None
		if targetList == None:
			self.targetList = cltypes.active
		else:
			self.targetList = targetList

class PlayReq:
	def __init__(self,uid,cardNum,playArgs,cardList=None):
		self.uid = uid
		self.cardNum = cardNum
		if self.cardList == None:
			self.cardList = cltypes.hand
		else:
			self.cardList = cardList
		self.playArgs = playArgs
