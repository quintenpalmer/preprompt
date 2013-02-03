from model import cltypes
from model.card_list import Card_List
from model.player import player_type

from model.errors import Game_Action_Error

class Collection:
	def __init__(self,cards=None):
		self.lists = []
		self.visibility = cltypes.Visibility()
		for i in xrange(0,cltypes.size):
			self.lists.append(Card_List())
		if cards != None:
			self.lists[cltypes.deck] = Card_List(cards)

	def xml_output(self,my_player_type):
		print my_player_type
		if my_player_type == player_type.me:
			index = 0
		elif my_player_type == player_type.them:
			index = 1
		else:
			raise Game_Action_Error('Player Type %s does not exist'%my_player_type)
		xml = '<lists>'
		for i in cltypes.full:
			xml += '<'+cltypes.names[i]+'>'
			full = self.visibility.visible[i][index]
			xml += self.lists[i].xml_output(full)
			xml += '</'+cltypes.names[i]+'>'
		xml += '</lists>'
		return xml

	def draw(self):
		try:
			card = self.lists[cltypes.deck].pop()
		except IndexError:
			raise Game_Action_Error('That player has no more cards in his/her deck')
		self.lists[cltypes.hand].push(card)

	def play_to_active(self,card_id):
		card = self.lists[cltypes.hand].pop(card_id)
		self.lists[cltypes.active].push(card)

	def play_to_grave(self,card_id):
		card = self.lists[cltypes.hand].pop(card_id)
		self.lists[cltypes.grave].push(card)
