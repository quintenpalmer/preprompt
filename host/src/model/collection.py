from src.model import cltypes
from src.model.card_list import Card_List
from src.model.player import player_type

class Collection:
	def __init__(self,cards=None):
		self.lists = []
		self.visibility = cltypes.Visibility()
		for i in xrange(0,cltypes.size):
			self.lists.append(Card_List())
		if cards != None:
			self.lists[cltypes.deck] = Card_List(cards)

	def xml_output(self,my_player_type):
		if my_player_type == player_type.me:
			index = 0
		elif my_player_type == player_type.them:
			index = 1
		out_str = ""
		out_str += "<lists>"
		for i in cltypes.full:
			out_str += "<"+cltypes.names[i]+">"
			full = self.visibility.visible[i][index]
			out_str += self.lists[i].xml_output(full)
			out_str += "</"+cltypes.names[i]+">"
		out_str += "</lists>"
		return out_str

	def draw(self):
		card = self.lists[cltypes.deck].pop()
		self.lists[cltypes.hand].push(card)

	def play_to_active(self,card_id):
		card = self.lists[cltypes.hand].pop(card_id)
		self.lists[cltypes.active].push(card)

	def play_to_grave(self,card_id):
		card = self.lists[cltypes.hand].pop(card_id)
		self.lists[cltypes.grave].push(card)
