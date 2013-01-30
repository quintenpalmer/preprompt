from src.control.load import database_reader
from src.model.game import Game

class Model:
	def __init__(self):
		self.games = {}
		self.free_ids = range(0,100)
		self.all_ids = list(self.free_ids)

	def start_game(self,config_args):
		game_id = self.pop_id()
		game = database_reader.get_game(config_args)
		self.games[game_id] = game
		return game_id

	def stop_game(self,game_id):
		try:
			del self.games[game_id]
			self.push_id(game_id)
		except IndexError:
			raise Exception("That is not a valid game id")

	def get_game_from_id(self,game_id):
		try:
			return self.games[game_id]
		except IndexError:
			raise Exception("That is not a valid game id")

	def pop_id(self):
		if len(self.free_ids) > 0:
			return self.free_ids.pop(0)
		else:
			raise Exception("No room for more games")

	def push_id(self,push_id):
		self.free_ids.append(push_id)

	def out(self,game_id,uid):
		return self.games[game_id].xml_output(uid)
