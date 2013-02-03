
class Player_Container:
	def __init__(self,player,collection):
		self.player = player
		self.collection = collection

	def xml_output(self,player_type):
		xml = '<player>%s</player>'%self.player.xml_output(player_type)
		xml += '<collection>%s</collection>'%self.collection.xml_output(player_type)
		return xml

class Player:
	def __init__(self,uid):
		self.uid = uid
		self.name = str(uid)
		self.health = 50

	def xml_output(self,player_type):
		xml = '<uid>%s</uid>'%str(self.uid)
		xml += '<name>%s</name>'%self.name
		xml += '<health>%s</health>'%str(self.health)
		return xml

class player_type:
	me = 0
	them = 1
