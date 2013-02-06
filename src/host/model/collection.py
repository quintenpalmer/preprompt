from model import cltypes
from model.card_list import Card_List
from model import player_type
from pyplib.errors import PP_Game_Action_Error
from pyplib.xml_parser import parse_element

class Collection:
	def __init__(self,**kwargs):
		if kwargs.has_key('cards'):
			cards = kwargs['cards']
			self.visibility = cltypes.Visibility()
			self.lists = []
			for i in xrange(0,cltypes.size):
				self.lists.append(Card_List())
			self.lists[cltypes.deck] = Card_List(cards=cards)
		elif kwargs.has_key('element'):
			element = kwargs['element']
			self.lists = range(cltypes.size)
			self.lists[cltypes.deck] = Card_List(element=parse_element(element,'deck'))
			self.lists[cltypes.hand] = Card_List(element=parse_element(element,'hand'))
			self.lists[cltypes.active] = Card_List(element=parse_element(element,'active'))
			self.lists[cltypes.grave] = Card_List(element=parse_element(element,'grave'))
			self.lists[cltypes.special] = Card_List(element=parse_element(element,'special'))
			self.lists[cltypes.other] = Card_List(element=parse_element(element,'other'))
			self.visibility = cltypes.Visibility(element=parse_element(element,'visibilities'))
		else:
			raise PP_Game_Action_Error("Collection construction had improper kwargs %s"%kwargs.keys())

	def xml_output(self,my_player_type):
		if my_player_type == player_type.full:
			index = 0
			full = True
		elif my_player_type == player_type.me:
			index = 1
			full = False
		elif my_player_type == player_type.them:
			index = 2
			full = False
		else:
			raise PP_Game_Action_Error('Player Type %s does not exist'%my_player_type)
		xml = '<lists>'
		for i in cltypes.full:
			xml += '<'+cltypes.names[i]+'>'
			vis = self.visibility.visible[i][index]
			xml += self.lists[i].xml_output(full,vis)
			xml += '</'+cltypes.names[i]+'>'
		xml += '</lists>'
		if index == 0:
			xml += '<visibilities>'
			xml += self.visibility.xml_output()
			xml += '</visibilities>'
		return xml

	def draw(self):
		try:
			card = self.lists[cltypes.deck].pop()
			self.lists[cltypes.hand].push(card)
		except IndexError:
			raise PP_Game_Action_Error('That player has no more cards in his/her deck')

	def play_to_active(self,card_id):
		card = self.lists[cltypes.hand].pop(card_id)
		self.lists[cltypes.active].push(card)

	def play_to_grave(self,card_id):
		card = self.lists[cltypes.hand].pop(card_id)
		self.lists[cltypes.grave].push(card)
