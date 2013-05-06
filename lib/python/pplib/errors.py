class XML_Parser_Error(Exception):
	def __init__(self,message):
		self.message = message
	def __str__(self):
		return self.message

class PP_Model_Error(Exception):
	def __init__(self,message):
		self.message = message
	def __str__(self):
		return self.message

class PP_Game_Action_Error(Exception):
	def __init__(self,message):
		self.message = message
	def __str__(self):
		return self.message

class PP_Load_Error(Exception):
	def __init__(self,message):
		self.message = message
	def __str__(self):
		return self.message

class PP_Database_Error(Exception):
	def __init__(self,message):
		self.message = message
	def __str__(self):
		return self.message

class JsonParserError(Exception):
	def __init__(self,message):
		self.message = message
	def __str__(self):
		return self.message
