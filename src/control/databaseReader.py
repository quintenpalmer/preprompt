from src.model.game.Game import Game
from src.model.player.PlayerContainer import PlayerContainer
from src.model.player.Player import Player
from src.model.card.Card import Card
from src.model.collection.Collection import Collection
from src.control.gameHandle.card.Effect import Effect

def getGame(startInfo):
	uids = startInfo[0]
	dids = startInfo[1]
	#TODO GET PLAYER DECK INFO FROM DATABASE
	cardNames = ['farts','fresh']
	players = []
	for i in xrange(0,2):
		player = Player(uids[i])
		cards = []
		for j in xrange(0,40):
			name = cardNames[i]
			effect = Effect(('o,d,f,1',))
			cards.append(Card(name,effect))
		playerCollection = Collection(cards)
		players.append(PlayerContainer(player,playerCollection))

	return Game(players[0],players[1])
