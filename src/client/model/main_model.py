from model.game import Game
from pyplib.xml_parser import parse_xml, parse_int, parse_element, parse_string
from pyplib.errors import PP_Model_Error
import util

class Model:
	def __init__(self,uid):
		self.games = {}
		self.logged_in_uid = uid
		self.current_game_id = None
		self.version = 0

	def update_game(self,resp):
		self.ele = parse_xml(resp)
		resp_status = parse_string(self.ele,'resp_status')
		if resp_status == 'ok':
			resp_type = parse_string(self.ele,'resp_type')
			game_id = parse_int(self.ele,'game_id')
			game_state = parse_element(self.ele,'game_xml')
			self.games[game_id] = Game(game_state)
			self.current_game_id = game_id
			return resp_type.title()+' was successful!'
		else:
			error_message = parse_string(self.ele,'error_message')
			if resp_status == 'bad_xml_request':
				util.logger.warning('Last Request had bad xml data: '+error_message)
			elif resp_status == 'invalid_game_action':
				util.logger.warning('Last Request had an invalid game action: '+error_message)
			elif resp_status == 'invalid_model_action':
				util.logger.warning('Last Request had an invalid model action: '+error_message)
			return 'Received error message: '+error_message

	def get_current_game(self):
		try:
			return self.games[self.current_game_id]
		except KeyError:
			raise PP_Model_Error('The current_game_id is not the id of a real game!')
