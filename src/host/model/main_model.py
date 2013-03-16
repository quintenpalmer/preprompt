from pyplib.errors import PP_Model_Error,PP_Load_Error,XML_Parser_Error,PP_Database_Error
from pyplib import util,database

from control import database_reader
from model import cltypes
from model.game import Game

class Model:
	def __init__(self,num_games):
		self.games = {}
		self.dead_games = {}
		self.user_map = {}
		self.game_count = 0;
		self.version = 0
		try:
			games = database.select('play_games','*')
			for game in games:
				game_id = game[0]
				game_xml = game[1]
				try:
					self.now_using(game_id)
					self.book_keep_game(game_id,Game(xml_string=game_xml))
				except XML_Parser_Error as e:
					util.logger.warn("Error loading %s's xml %s"%(str(game_file_name),str(e)))
		except IOError or ValueError:
			util.logger.error("Error reading game data")
			raise PP_Load_Error("Save File could not be opened")

	def start_game(self,config_args):
		game_id = self.get_next_id()
		game = database_reader.get_game(config_args)
		print dir(game)
		for player in game.players:
			player.collection.lists[cltypes.deck].shuffle()
		try:
			database.insert('play_games',(int,str),(game_id,game.xml_output(0)))
		except PP_Database_Error:
			util.logger.error("Error writing game data")
			raise PP_Load_Error("Save File %s could not be opened"%str(game_id))
		self.book_keep_game(game_id,game)
		return game_id

	def book_keep_game(self,game_id,game):
		uid1 = game.players[0].player.uid
		uid2 = game.players[1].player.uid
		if self.user_map.has_key(uid1):
			self.user_map[uid1].append(game_id)
		else:
			self.user_map[uid1] = [game_id]
		if self.user_map.has_key(uid2):
			self.user_map[uid2].append(game_id)
		else:
			self.user_map[uid2] = [game_id]
		self.games[game_id] = game

	def book_keep_remove_game(self,game_id,game):
		uid1 = game.players[0].player.uid
		uid2 = game.players[1].player.uid
		del self.user_map[uid1][game_id]
		del self.user_map[uid2][game_id]
		del self.games[game_id]

	def verify_game(self,game_id):
		end_stats = self.get_game_from_id(game_id).has_ended()
		if end_stats[0]:
			winner = end_stats[1]
			self.stop_game(game_id);
		return end_stats

	def stop_game(self,game_id):
		try:
			self.book_keep_remove_game(game_id,self.games[game_id])
		except IndexError:
			raise PP_Model_Error("%s is not a valid game id"%str(game_id))

	def get_game_from_id(self,game_id):
		try:
			return self.games[game_id]
		except KeyError:
			raise PP_Model_Error("%s is not a valid game id"%str(game_id))

	def get_games_from_uid(self,uid):
		try:
			return self.user_map[uid]
		except KeyError:
			return []

	def get_next_id(self):
		ret_id = self.game_count
		self.game_count += 1
		return ret_id

	def now_using(self,game_id):
		if game_id > self.game_count:
			self.game_count = game_id + 1

	def out(self,game_id,uid):
		return self.get_game_from_id(game_id).xml_output(uid)
