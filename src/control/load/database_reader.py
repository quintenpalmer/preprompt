from src.model.game.Game import Game
from src.model.player.Player_Container import Player_Container
from src.model.player.Player import Player
from src.model.card.Card import Card
from src.model.collection.Collection import Collection

from src.control.load.Effects import getDirect_Damage
from src.control.load.Effects import getSits_NTurns

def getGame(config_args):
	player1 = config_args.config_player1
	player2 = config_args.config_player2
	uids = [player1.uid,player2.uid]
	dids = [player1.did,player2.did]
	#TODO GET PLAYER DECK INFO FROM DATABASE
	cardNames = ['farts','fresh','persist']
	players = []
	for i in xrange(0,2):
		player = Player(uids[i])
		cards = []
		name = cardNames[2]
		effect = getSits_NTurns('water',3)
		cards.append(Card(name,effect))
		for j in xrange(0,39):
			name = cardNames[i]
			effect = getDirect_Damage('fire',4)
			cards.append(Card(name,effect))
		playerCollection = Collection(cards)
		players.append(Player_Container(player,playerCollection))

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
