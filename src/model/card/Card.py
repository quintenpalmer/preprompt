
class Card:
	def __init__(self,name,effect):
		self.name = name
		self.effect = effect

	def xmlOutput(self):
		outStr = ""
		outStr +="<name>"
		outStr += self.name
		outStr +="</name>"
		return outStr

	def play(self,args):
		self.effect(args)
