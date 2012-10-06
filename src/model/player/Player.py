
class Player:
	def __init__(self,uid):
		self.uid = uid
		self.name = str(uid)
		self.health = 50

	def xmlOutput(self,playerType):
		outStr = ""
		outStr += "<uid>"
		outStr += str(self.uid)
		outStr += "</uid>"
		outStr += "<name>"
		outStr += self.name
		outStr += "</name>"
		outStr += "<health>"
		outStr += str(self.health)
		outStr += "</health>"
		return outStr
