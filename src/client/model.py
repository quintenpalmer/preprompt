from pplib.json_parser import PPjo

class Model:
	def __init__(self,uid):
		self.games = {}
		self.logged_in_uid = uid
		self.current_game_id = None
		self.version = 0

	def update_game(self,resp):
		#with open("ASDF.json","w") as f:
		#	f.write(str(resp))
		obj = PPjo(resp)
		respType = obj.get_string("respType")
		if respType == "ok":
			command = obj.get_string("command")
			gameId = obj.get_int("gameId")
			message = obj.get_string("message")
			gameRepr = obj.get_object("gameRepr")
			self.games[gameId] = Game(gameRepr.get_object("game"))
			self.current_game_id = gameId
			return message
		else:
			return 'Received error message: %s'%respType

	def get_current_game(self):
		return self.games[self.current_game_id]

class Game:
	def __init__(self,obj):
		self.me = Player_Container(obj.get_object('me'))
		self.them = Player_Container(obj.get_object('them'))
		self.super_phase = obj.get_int('superPhase')
		self.phase = obj.get_int('phase')
		self.turn_owner = obj.get_int('turnOwner')
		self.has_drawn = obj.get_bool('hasDrawn')

class Player_Container:
	def __init__(self,obj):
		self.uid = obj.get_int('uid')
		self.name = obj.get_string('name')
		self.health = obj.get_int('health')
		self.deck    = Card_List(obj.get_object('deck'))
		self.hand    = Card_List(obj.get_object('hand'))
		self.active  = Card_List(obj.get_object('active'))
		self.grave   = Card_List(obj.get_object('grave'))
		self.special = Card_List(obj.get_object('special'))

class Card_List:
	def __init__(self,obj):
		self.cards = []
		for card_element in obj.get_objects('cards'):
			self.cards.append(Card(card_element))

class Card:
	def __init__(self,obj):
		card = obj.get_object('card')
		self.name = card.get_string('name')
