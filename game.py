from src.model.model import Model
from src.model.clist import cltypes
from src.control.game_logic.play.play import Play_Args
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
	game_id1 = model.start_game(Config_Args(config_player1,config_player2))

	# Draw a card
	model.games[game_id1].draw(p1uid)

	# Play a card from player 1's hand targetting player 2's first active card
	play_args = Play_Args(
		game=model.games[game_id1].game,
		src_uid=p1uid,
		src_card=0,
		src_list=cltypes.hand,
		tgt_uid=p2uid,
		tgt_card=0,
		tgt_list=cltypes.active)
	model.games[game_id1].play(play_args)

	# Print the game from player 1's perspective
	print model.out(p1uid)
	# Stop the game
	model.stop_game(game_id1)

	#control = Controller(model)
	#disp = Display(model)
