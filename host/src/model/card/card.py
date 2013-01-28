
class Card:
	def __init__(self,name,effect):
		self.name = name
		self.effect = effect

	def xml_output(self):
		out_str = ""
		out_str +="<name>"
		out_str += self.name
		out_str +="</name>"
		return out_str

	def play(self,args):
		self.effect(args)
