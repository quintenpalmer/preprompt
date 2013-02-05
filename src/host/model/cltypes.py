from model.errors import Game_Action_Error

from pyplib.xml_parser import parse_bool,parse_element

deck = 0
hand = 1
active = 2
grave = 3
special = 4
other = 5

names = {}
names[deck]='deck'
names[hand]='hand'
names[active]='active'
names[grave]='grave'
names[special]='special'
names[other]='other'

values = {}
values['deck']=deck
values['hand']=hand
values['active']=active
values['grave']=grave
values['special']=special
values['other']=other

size = len(names)

full = range(0,size)

class Visibility:
	def __init__(self,**kwargs):
		if len(kwargs) == 0:
			self.visible = range(0,size)
			self.visible[deck] = (True,False,False)
			self.visible[hand] = (True,True,False)
			self.visible[active] = (True,True,True)
			self.visible[grave] = (True,True,True)
			self.visible[special] = (True,False,False)
			self.visible[other] = (True,True,False)
		elif kwargs.has_key('element'):
			element = kwargs['element']
			self.visible = range(0,size)
			deck_element = parse_element(element,names[deck])
			self.visible[deck] = (True,parse_bool(deck_element,'me_vis'),parse_bool(deck_element,'them_vis'))
			hand_element = parse_element(element,names[hand])
			self.visible[hand] = (True,parse_bool(hand_element,'me_vis'),parse_bool(hand_element,'them_vis'))
			active_element = parse_element(element,names[active])
			self.visible[active] = (True,parse_bool(active_element,'me_vis'),parse_bool(active_element,'them_vis'))
			grave_element = parse_element(element,names[grave])
			self.visible[grave] = (True,parse_bool(grave_element,'me_vis'),parse_bool(grave_element,'them_vis'))
			special_element = parse_element(element,names[special])
			self.visible[special] = (True,parse_bool(special_element,'me_vis'),parse_bool(special_element,'them_vis'))
			other_element = parse_element(element,names[other])
			self.visible[other] = (True,parse_bool(other_element,'me_vis'),parse_bool(other_element,'them_vis'))
		else:
			raise Game_Action_Error("Visibility instantiated with invalid constructor %s"%str(kwargs))

	def xml_output(self):
		xml = ''
		for i,vis in enumerate(self.visible):
			xml += '<'+names[i]+'>'
			xml += '<me_vis>'+str(vis[1])+'</me_vis>'
			xml += '<them_vis>'+str(vis[2])+'</them_vis>'
			xml += '</'+names[i]+'>'
		return xml
