from src.model.game.game import Game
from src.control.xml_parser import parse_xml, parse_int, parse_element

class Model:
	def __init__(self):
		self.games = {}
		self.game_ids = []
		self.current_game = None

	def add_game(self,resp):
		self.ele = parse_xml(resp)
		game_id = parse_int(self.ele,'param0')
		game_state = parse_element(self.ele,'param1')
		self.games[game_id] = Game(game_state)
		self.game_ids.append(game_id)
		self.current_game = (game_id,self.games[game_id])
