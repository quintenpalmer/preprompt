from src.model.game import Game
from pyplib.xml_parser import parse_xml, parse_int, parse_element

class Model:
	def __init__(self):
		self.games = {}
		self.game_ids = []
		self.logged_in_uid = 26
		self.current_game_id = None

	def add_game(self,resp):
		self.ele = parse_xml(resp)
		game_id = parse_int(self.ele,'param1')
		game_state = parse_element(self.ele,'param2')
		self.games[game_id] = Game(game_state)
		self.game_ids.append(game_id)
		self.current_game_id = game_id
	
	def update_game(self,resp):
		self.ele = parse_xml(resp)
		game_id = parse_int(self.ele,'param1')
		game_state = parse_element(self.ele,'param2')
		self.games[game_id] = Game(game_state)
		self.current_game_id = game_id

	def get_current_game(self):
		return self.games[self.current_game_id]
