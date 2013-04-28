from pplib.errors import PP_Game_Action_Error
from pplib.xml_parser import parse_xml, parse_element

from model import player_type
from model.player import Player_Container
from model.control_state import Control_State,super_phase,phase
from model.action import Action

class Game:
	def __init__(self,**kwargs):
		if kwargs.has_key('player1') and kwargs.has_key('player2'):
			player1 = kwargs['player1']
			player2 = kwargs['player2']
			self.players = []
			self.players.append(player1)
			self.players.append(player2)
			self.control_state = Control_State()
		elif kwargs.has_key('xml_string'):
			raw_element = parse_xml(kwargs['xml_string'])
			element = parse_element(raw_element,'game')
			self.players = []
			self.players.append(Player_Container(element=parse_element(element,'me')))
			self.players.append(Player_Container(element=parse_element(element,'them')))
			self.control_state = Control_State(element=parse_element(element,'control_state'))
		else:
			raise PP_Game_Action_Error("Game Instantiated without correct args")

	def get_me_from_uid(self,uid):
		if self.players[0].player.uid == uid:
			return self.players[0]
		elif self.players[1].player.uid == uid:
			return self.players[1]
		else:
			raise PP_Game_Action_Error("Not the uid of a player playing this game:"+str(uid))

	def get_them_from_uid(self,uid):
		if self.players[0].player.uid == uid:
			return self.players[1]
		elif self.players[1].player.uid == uid:
			return self.players[0]
		else:
			raise PP_Game_Action_Error("Not the uid of a player playing this game:"+str(uid))

	def get_index_from_uid(self,uid):
		if self.players[0].player.uid == uid:
			return 0
		elif self.players[1].player.uid == uid:
			return 1
		else:
			raise PP_Game_Action_Error("Not the uid of a player playing this game:"+str(uid))

	def get_current_turn_owner(self):
		return self.players[self.control_state.turn_owner].player.uid

	def xml_output(self,uid):
		if uid == 0:
			me_player_type = player_type.full
			them_player_type = player_type.full
			me_uid = self.players[0].player.uid
			full = True
		else:
			me_player_type = player_type.me
			them_player_type = player_type.them
			me_uid = uid
			full = False

		me_index = self.get_index_from_uid(me_uid)
		them_uid = self.get_them_from_uid(me_uid).player.uid
		them_index = self.get_index_from_uid(them_uid)

		xml = '<game>'
		xml += '<me>%s</me>'%self.get_me_from_uid(me_uid).xml_output(me_player_type)
		xml += '<them>%s</them>'%self.get_them_from_uid(me_uid).xml_output(them_player_type)
		xml += '<control_state>%s</control_state>'%self.control_state.xml_output(me_uid,me_index,them_uid,them_index,full)
		xml += '</game>'
		return xml

	def verify_main_super_phase(self,action):
		if not self.control_state.super_phase == super_phase.main:
			raise PP_Game_Action_Error("%s can only be performed in the regular gameplay super phase"%action)

	def verify_setup_super_phase(self,action):
		if not self.control_state.super_phase == super_phase.setup:
			raise PP_Game_Action_Error("%s can only be performed in the setup super phase"%action)

	def verify_current_turn_owner(self,uid,action):
		if not self.get_current_turn_owner() == uid:
			raise PP_Game_Action_Error("Player %s cannot conduct %s during this turn"%(str(uid),action))

	def check_game_end(self):
		dead = []
		for player in self.players:
			if player.player.health <= 0:
				dead.append(player.player.uid)
				self.control_state.super_phase = super_phase.end
		if len(dead) == 1:
			return [True,dead[0]]
		elif len(dead) == 0:
			return [False,None]
		else:
			return [True,None]
