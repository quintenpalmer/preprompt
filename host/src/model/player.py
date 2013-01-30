
class Player_Container:
	def __init__(self,player,collection):
		self.player = player
		self.collection = collection

	def xml_output(self,player_type):
		out_str = ""
		out_str += "<player>"
		out_str += self.player.xml_output(player_type)
		out_str += "</player>"
		out_str += "<collection>"
		out_str += self.collection.xml_output(player_type)
		out_str += "</collection>"
		return out_str
	def __repr__(self):
		return "Player: "+self.player.name+","+str(self.player.health)

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

class player_type:
	me = 0
	them = 1
