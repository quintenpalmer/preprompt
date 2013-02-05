from control import database_reader
from model.game import Game

from model.errors import Model_Error
from pyplib.xml_parser import XML_Parser_Error

import util
import os

class Model:
	def __init__(self,num_games):
		self.games = {}
		self.free_ids = range(0,num_games)
		self.all_ids = list(self.free_ids)
		try:
			game_file_dir = os.path.join(os.environ['pyp'],'data','games')
			game_file_names = os.listdir(game_file_dir)
			for game_file_name in game_file_names:
				if game_file_name != '__init__.py':
					game_id = int(game_file_name.split('.')[0])
					game_file = open(os.path.join(game_file_dir,game_file_name),'r')
					try:
						xml_string = game_file.readlines()[0]
					except IndexError:	
						util.logger.warn("File %s has no data in it"%str(game_file_name))
					try:
						self.games[game_id] = Game(xml_string=xml_string)
						self.free_ids.remove(game_id)
					except XML_Parser_Error as e:
						util.logger.warn("Error loading %s's xml %s"%(str(game_file_name),str(e)))
					game_file.close()
		except IOError, ValueError:
			util.logger.error("Error reading game data")
			raise Model_Error("Save File could not be opened","internal_error")

	def start_game(self,config_args):
		game_id = self.pop_id()
		game = database_reader.get_game(config_args)
		try:
			path = os.path.join(os.environ['pyp'],'data','games',str(game_id)+'.save')
			game_file = open(path,'w')
			game_file.write(game.xml_output(0))
			game_file.close()
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
