from pyplib.errors import PP_Game_Action_Error
from pyplib.xml_parser import parse_element,parse_bool

from model import cltypes
from model import player_type
from model.card_list import Card_List

class Collection:
	def __init__(self,**kwargs):
		if kwargs.has_key('cards'):
			cards = kwargs['cards']
			self.visibility = Visibility()
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
			self.visibility = Visibility(element=parse_element(element,'visibilities'))
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

class Visibility:
	def __init__(self,**kwargs):
		if len(kwargs) == 0:
			self.visible = range(0,cltypes.size)
			self.visible[cltypes.deck] = (True,False,False)
			self.visible[cltypes.hand] = (True,True,False)
			self.visible[cltypes.active] = (True,True,True)
			self.visible[cltypes.grave] = (True,True,True)
			self.visible[cltypes.special] = (True,False,False)
			self.visible[cltypes.other] = (True,True,False)
		elif kwargs.has_key('element'):
			element = kwargs['element']
			self.visible = range(0,cltypes.size)
			deck_element = parse_element(element,cltypes.names[cltypes.deck])
			self.visible[cltypes.deck] = (True,parse_bool(deck_element,'me_vis'),parse_bool(deck_element,'them_vis'))
			hand_element = parse_element(element,cltypes.names[cltypes.hand])
			self.visible[cltypes.hand] = (True,parse_bool(hand_element,'me_vis'),parse_bool(hand_element,'them_vis'))
			active_element = parse_element(element,cltypes.names[cltypes.active])
			self.visible[cltypes.active] = (True,parse_bool(active_element,'me_vis'),parse_bool(active_element,'them_vis'))
			grave_element = parse_element(element,cltypes.names[cltypes.grave])
			self.visible[cltypes.grave] = (True,parse_bool(grave_element,'me_vis'),parse_bool(grave_element,'them_vis'))
			special_element = parse_element(element,cltypes.names[cltypes.special])
			self.visible[cltypes.special] = (True,parse_bool(special_element,'me_vis'),parse_bool(special_element,'them_vis'))
			other_element = parse_element(element,cltypes.names[cltypes.other])
			self.visible[cltypes.other] = (True,parse_bool(other_element,'me_vis'),parse_bool(other_element,'them_vis'))
		else:
			raise PP_Game_Action_Error("Visibility instantiated with invalid constructor %s"%str(kwargs))

	def xml_output(self):
		xml = ''
		for i,vis in enumerate(self.visible):
			xml += '<'+cltypes.names[i]+'>'
			xml += '<me_vis>'+str(vis[1])+'</me_vis>'
			xml += '<them_vis>'+str(vis[2])+'</them_vis>'
			xml += '</'+cltypes.names[i]+'>'
		return xml
