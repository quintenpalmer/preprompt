from src.control.load import database_reader
from src.control.game_logic.game_control import Game_Control

class Model:
	def __init__(self):
		self.games = {}
		self.free_ids = range(0,100)

	def start_game(self,config_args):
		game = database_reader.get_game(config_args)
		game_id = self.pop_id()
		self.games[game_id] = Game_Control(game)
		return game_id

	def stop_game(self,game_id):
		del self.games[game_id]
		self.push_id(game_id)

	def pop_id(self):
		if len(self.free_ids) > 0:
			return self.free_ids.pop(0)
		else:
			raise Exception("No room for more games")

	def push_id(self,push_id):
		self.free_ids.append(push_id)

	def out(self,uid):
		for val in self.games.itervalues():
			return val.game.xml_output(uid)
