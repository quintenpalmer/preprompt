from src.model.Model import Model
from src.model.clist import cltypes
from src.control.game_logic.play.Play import Play_Args
from src.control.load.database_reader import Config_Player, Config_Args
#from src.control import Controller
#from src.view import Display

if __name__ == '__main__':
	# Make the model to start (this HAS to happen)
	model = Model()
	# Make the config players (what will be loaded from the db
	p1uid = 26
	p2uid = 13
	config_player1 = Config_Player(p1uid,1,'Prompt')
	config_player2 = Config_Player(p2uid,2,'Post')

	# Make the game
	gameId1 = model.startGame(Config_Args(config_player1,config_player2))

	# Draw a card
	model.games[gameId1].draw(p1uid)

	# Play a card from player 1's hand targetting player 2's first active card
	playArgs = Play_Args(
		game=model.games[gameId1].game,
		srcUid=p1uid,
		srcCard=0,
		srcList=cltypes.hand,
		tgtUid=p2uid,
		tgtCard=0,
		tgtList=cltypes.active)
	model.games[gameId1].play(playArgs)

	# Print the game from player 1's perspective
	print model.out(p1uid)
	# Stop the game
	model.stopGame(gameId1)

	#control = Controller(model)
	#disp = Display(model)
