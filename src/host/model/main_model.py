from control.load import database_reader
from model.game import Game

from model.errors import Model_Error

import util
from os import environ

class Model:
	def __init__(self,num_games):
		self.games = {}
		self.free_ids = range(0,num_games)
		self.all_ids = list(self.free_ids)

	def start_game(self,config_args):
		game_id = self.pop_id()
		game = database_reader.get_game(config_args)
		try:
			save_files = open(environ['pyp']+'/data/games/'+str(game_id)+'.save','w')
		except IOError:
			util.logger.error("Error writing game data")
			raise Model_Error("Save File %s could not be opened"%(str(game_id),),"internal_error")
		self.games[game_id] = game
		return game_id

	def stop_game(self,game_id):
		try:
			del self.games[game_id]
			self.push_id(game_id)
		except IndexError:
			raise Model_Error("%s is not a valid game id"%(str(game_id),),"invalid_game_id")

	def get_game_from_id(self,game_id):
		try:
			return self.games[game_id]
		except IndexError:
			raise Model_Error("%s is not a valid game id"%(str(game_id),),"invalid_game_id")

	def pop_id(self):
		if len(self.free_ids) > 0:
			return self.free_ids.pop(0)
		else:
			raise Model_Error("No More room for games","game_count_limit")

	def push_id(self,push_id):
		self.free_ids.append(push_id)

	def out(self,game_id,uid):
		return self.get_game_from_id(game_id).xml_output(uid)
