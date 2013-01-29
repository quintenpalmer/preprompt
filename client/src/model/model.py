from src.control.xml_parser import parse_game_from_xml

class Model:
	def __init__(self):
		self.games = {}
		self.game_ids = []
		self.current_game = None

	def add_game(self,game_id,xml_string):
		self.games[game_id] = parse_game_from_xml(xml_string)
		self.game_ids.append(game_id)
