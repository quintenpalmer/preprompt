from model.game import Game
from model.player import Player_Container, Player
from model.collection import Collection

from control.load.loaded_effects import lookup_table 

import os

def get_game(config_args):
	player1 = config_args.config_player1
	player2 = config_args.config_player2
	uids = [player1.uid,player2.uid]
	dids = [player1.did,player2.did]
	#TODO GET PLAYER DECK INFO FROM DATABASE
	card_names = ['farts','fresh','persist']
	players = []
	for i in range(0,2):
		player = Player(uid=uids[i])
		cards = []
		path = os.path.join(os.environ['pyp'],'data','players',str(uids[i]),str(dids[i])+'.cards')
		f = open(path,'r')
		deck = [x.strip() for x in f.readlines()[0].split(',')]
		f.close()
		for lookup_string in deck:
			cards.append(lookup_table(lookup_string))
		player_collection = Collection(cards=cards)
		players.append(Player_Container(player=player,collection=player_collection))

	return Game(player1=players[0],player2=players[1])
