from pplib import json_parser
from pplib import util
from pplib.errors import PP_Model_Error

from game import Game

class Model:
	def __init__(self,uid):
		self.games = {}
		self.logged_in_uid = uid
		self.current_game_id = None
		self.version = 0

	def update_game(self,resp):
		with open("ASDF.json","w") as f:
			f.write(str(resp))
		obj = json_parser.create_object(resp)
		respType = json_parser.get_string(obj,"respType")
		print '------------'
		print respType
		print '------------'
		if respType == "ok":
			command = json_parser.get_string(obj,"command")
			gameId = json_parser.get_int(obj,"gameId")
			message = json_parser.get_string(obj,"message")
			print message
			print gameId
			gameRepr = json_parser.get_object(obj,"gameRepr")
			print type(gameRepr)
			self.games[gameId] = Game(json_parser.get_object(gameRepr,"game"))
			self.current_game_id = gameId
			return command.title()+' was successful!'
		else:
			return 'Received error message: %s'%respType

	def get_current_game(self):
		try:
			return self.games[self.current_game_id]
		except KeyError:
			raise PP_Model_Error('The current_game_id is not the id of a real game!')
