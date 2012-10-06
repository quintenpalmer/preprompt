
class PlayerContainer:
	def __init__(self,player,collection):
		self.player = player
		self.collection = collection

	def xmlOutput(self,playerType):
		outStr = ""
		outStr += "<player>"
		outStr += self.player.xmlOutput(playerType)
		outStr += "</player>"
		outStr += "<collection>"
		outStr += self.collection.xmlOutput(playerType)
		outStr += "</collection>"
		return outStr
