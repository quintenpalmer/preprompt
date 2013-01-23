
class Player:
	def __init__(self,uid):
		self.uid = uid
		self.name = str(uid)
		self.health = 50

	def xml_output(self,player_type):
		out_str = ""
		out_str += "<uid>"
		out_str += str(self.uid)
		out_str += "</uid>"
		out_str += "<name>"
		out_str += self.name
		out_str += "</name>"
		out_str += "<health>"
		out_str += str(self.health)
		out_str += "</health>"
		return out_str
