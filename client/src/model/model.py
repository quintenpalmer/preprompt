from src.model.game.game import Game

class Model:
	def __init__(self):
		self.games = {}
		self.game_ids = []
		self.current_game = None

	def add_game(self,game_id,xml_string):
		self.games[game_id] = Game(xml_string)
		self.game_ids.append(game_id)
