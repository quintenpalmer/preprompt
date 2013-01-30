from src.model import cltypes

class Play_Args:
	def __init__(self,game,src_uid,src_card,src_list,tgt_uid,tgt_card,tgt_list):
		self.game = game
		self.src_uid = src_uid
		self.src_card = src_card
		self.src_list = src_list

		self.tgt_uid = tgt_uid
		self.tgt_card = tgt_card
		self.tgt_list = tgt_list
