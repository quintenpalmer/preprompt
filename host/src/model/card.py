
class Card:
	def __init__(self,name,effect):
		self.name = name
		self.effect = effect

	def xml_output(self):
		xml = '<type>full</type>'
		xml += '<name>%s</name>'%self.name
		return xml

	def play(self,args):
		self.effect(args)

class Empty_Card:
	def xml_output(self):
		xml = "<type>empty</type>"
		return xml
