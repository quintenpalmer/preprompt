from src.model.game.game import Game
from src.model.player.player_container import Player_Container
from src.model.player.player import Player
from src.model.card.card import Card
from src.model.collection.collection import Collection

from src.control.load.loaded_effects import get_direct_damage
from src.control.load.loaded_effects import get_sits_nTurns

def get_game(config_args):
	player1 = config_args.config_player1
	player2 = config_args.config_player2
	uids = [player1.uid,player2.uid]
	dids = [player1.did,player2.did]
	#TODO GET PLAYER DECK INFO FROM DATABASE
	card_names = ['farts','fresh','persist']
	players = []
	for i in range(0,2):
		player = Player(uids[i])
		cards = []
		for j in range(0,9):
			name = card_names[i]
			effect = get_direct_damage('fire',4)
			cards.append(Card(name,effect))
		name = card_names[2]
		effect = get_sits_nTurns('water',3)
		cards.append(Card(name,effect))
		player_collection = Collection(cards)
		players.append(Player_Container(player,player_collection))

	return Game(players[0],players[1])

class Config_Args:
	def __init__(self,config_player1,config_player2,config_player3=None,config_player4=None):
		self.config_player1 = config_player1
		self.config_player2 = config_player2

class Config_Player:
	def __init__(self,uid,did,name):
		self.uid = uid
		self.did = did
		self.name = name
