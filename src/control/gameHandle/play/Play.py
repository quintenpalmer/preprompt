from src.model.clist import cltypes

class PlayArgs:
	def __init__(self,game,uid,targetCard=None,targetList=None):
		player = game.getMeFromUid(uid)
		clist = None
		if targetList == None:
			self.targetList = cltypes.hand

class PlayReq:
	def __init__(self,uid,cardList=None,cardNum=None,playArgs=None):
		self.uid = uid
		self.cardList = cardList
		self.cardNum = cardNum
		self.playArgs = playArgs
