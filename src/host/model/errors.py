class Model_Error(Exception):
	def __init__(self,message,status):
		self.message = message
		self.status  = status
	def __str__(self):
		return self.message

class Game_Action_Error(Exception):
	def __init__(self,message):
		self.message = message
	def __str__(self):
		return self.message
