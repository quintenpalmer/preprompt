from src.model.game.Game import Game
from src.model.player.PlayerContainer import PlayerContainer
from src.model.player.Player import Player
from src.model.card.Card import Card
from src.model.collection.Collection import Collection

from src.control.load.effects.Instants import getDirectDamage
from src.control.load.effects.Persists import SitsForever

def getGame(startInfo):
	uids = startInfo[0]
	dids = startInfo[1]
	#TODO GET PLAYER DECK INFO FROM DATABASE
	cardNames = ['farts','fresh','persist']
	players = []
	for i in xrange(0,2):
		player = Player(uids[i])
		cards = []
		#name = cardNames[2]
		#effect = SitsForever()
		#cards.append(Card(name,effect))
		for j in xrange(0,39):
			name = cardNames[i]
			effect = getDirectDamage('fire',4)
			cards.append(Card(name,effect))
		playerCollection = Collection(cards)
		players.append(PlayerContainer(player,playerCollection))

	return Game(players[0],players[1])
