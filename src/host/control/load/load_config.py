class Config_Args:
	def __init__(self,config_player1,config_player2,config_player3=None,config_player4=None):
		self.config_player1 = config_player1
		self.config_player2 = config_player2

class Config_Player:
	def __init__(self,uid,did):
		self.uid = uid
		self.did = did
