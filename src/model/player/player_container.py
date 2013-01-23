
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
