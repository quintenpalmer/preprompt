from src.model.game import Game
from src.model.player import Player_Container, Player
from src.model.collection import Collection

from src.control.load.loaded_effects import lookup_table 

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
		f = open('player_data/'+str(uids[i])+'/'+str(dids[i])+'.cards','r')
		deck = [x.strip() for x in f.readlines()[0].split(',')]
		f.close()
		for lookup_string in deck:
			cards.append(lookup_table(lookup_string))
		player_collection = Collection(cards)
		players.append(Player_Container(player,player_collection))

	return Game(players[0],players[1])

class Config_Args:
	def __init__(self,config_player1,config_player2,config_player3=None,config_player4=None):
		self.config_player1 = config_player1
		self.config_player2 = config_player2

class Config_Player:
	def __init__(self,uid,did):
		self.uid = uid
		self.did = did
