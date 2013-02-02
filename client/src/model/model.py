from src.model.game import Game
from pyplib.xml_parser import parse_xml, parse_int, parse_element, parse_string
from src import util

class Model:
	def __init__(self):
		self.games = {}
		self.game_ids = []
		self.logged_in_uid = 26
		self.current_game_id = None
		self.version = 0

	def update_game(self,resp):
		self.ele = parse_xml(resp)
		resp_status = parse_string(self.ele,'resp_status')
		print resp_status
		resp_type = parse_string(self.ele,'resp_type')
		print resp_type
		if resp_status == 'ok':
			game_id = parse_int(self.ele,'param_0')
			game_state = parse_element(self.ele,'param_1')
			print game_state
			self.games[game_id] = Game(game_state)
			self.current_game_id = game_id
		else:
			error_message = parse_string(self.ele,'resp_type')
			if resp_status == 'bad_xml_request':
				util.logger.warning('Last Request had bad xml data: '+error_message)
			elif resp_status == 'invalid_game_action':
				util.logger.warning('Last Request had an invalid game action: '+error_message)
			elif resp_status == 'invalid_model_action':
				util.logger.warning('Last Request had an invalid model action: '+error_message)
			print "Something went wrong"

	def get_current_game(self):
		return self.games[self.current_game_id]
