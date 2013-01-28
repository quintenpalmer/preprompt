from src.model.model import Model
from src.model.clist import cltypes
from src.control.game_logic.play import Play_Args
from src.control.load.database_reader import Config_Player, Config_Args
#from src.control import Controller
#from src.view import Display
from xml.dom.minidom import parseString

if __name__ == '__main__':
	# Make the model to start (this HAS to happen)
	model = Model()
	# Make the config players (what will be loaded from the db)
	p1uid = 26
	p2uid = 13
	config_player1 = Config_Player(p1uid,0,'Prompt')
	config_player2 = Config_Player(p2uid,1,'Post')

	# Make the game
	game_id1 = model.start_game(Config_Args(config_player1,config_player2))
	game = model.games[game_id1]

	game.setup()

	# Draw a card
	game.draw(p1uid)

	# Move out of the draw-phase
	game.step_phase()
	# Move out of the pre-phase
	game.step_phase()

	# Play a card from player 1's hand targetting player 2's first active card
	print game
	play_args = Play_Args(
		game=game,
		src_uid=p1uid,
		src_card=0,
		src_list=cltypes.hand,
		tgt_uid=p2uid,
		tgt_card=0,
		tgt_list=cltypes.active)
	game.play(play_args)

	# Play a card from player 1's hand targetting player 2's first active card
	play_args = Play_Args(
		game=game,
		src_uid=p1uid,
		src_card=0,
		src_list=cltypes.hand,
		tgt_uid=p2uid,
		tgt_card=0,
		tgt_list=cltypes.active)
	game.play(play_args)

	# Change the phase
	game.step_phase()
	game.toggle_turn()

	game.draw(p2uid)
	game.step_phase()
	game.step_phase()

	play_args = Play_Args(
		game=game,
		src_uid=p2uid,
		src_card=0,
		src_list=cltypes.hand,
		tgt_uid=p1uid,
		tgt_card=0,
		tgt_list=cltypes.active)
	game.play(play_args)

	play_args = Play_Args(
		game=game,
		src_uid=p2uid,
		src_card=0,
		src_list=cltypes.hand,
		tgt_uid=p1uid,
		tgt_card=0,
		tgt_list=cltypes.active)
	game.play(play_args)

	# Print the game from player 1's perspective
	print parseString(model.out(game_id1,p1uid)).toprettyxml(indent='  ')

	# Stop the game
	#model.stop_game(game_id1)

	#control = Controller(model)
	#disp = Display(model)
