from src.model.model import Model
from src.model.clist import cltypes
from src.control.game_logic.play import Play_Args
from src.control.load.database_reader import Config_Player, Config_Args
from src.control.network.network_host import Listener
#from src.view import Display
from xml.dom.minidom import parseString

if __name__ == '__main__':
	model = Model()
	listener = Listener()
	listener.listen_for_requests(model)
	'''
	p1uid = 26
	p2uid = 13
	config_player1 = Config_Player(p1uid,0)
	config_player2 = Config_Player(p2uid,1)

	game_id1 = model.start_game(Config_Args(config_player1,config_player2))
	game = model.get_game_from_id(game_id1)
	game.setup()
	game.draw(p1uid)
	game.step_phase()
	game.step_phase()
	game.play(Play_Args(
		game=game,
		src_uid=p1uid,
		src_list=cltypes.hand,
		src_card=0,
		tgt_uid=p2uid,
		tgt_list=cltypes.active,
		tgt_card=0))
	play(Play_Args(
		game=game,
		src_uid=p1uid,
		src_list=cltypes.hand,
		src_card=0,
		tgt_uid=p2uid,
		tgt_list=cltypes.active,
		tgt_card=0))
	game.step_phase()
	game.toggle_turn()
	game.draw(p2uid)
	game.step_phase()
	game.step_phase()
	play(Play_Args(
		game=game,
		src_uid=p2uid,
		src_card=0,
		src_list=cltypes.hand,
		tgt_uid=p1uid,
		tgt_list=cltypes.active,
		tgt_card=0))
	play(Play_Args(
		game=game,
		src_uid=p2uid,
		src_list=cltypes.hand,
		src_card=0,
		tgt_uid=p1uid,
		tgt_list=cltypes.active,
		tgt_card=0))
	print parseString(model.out(game_id1,p1uid)).toprettyxml(indent='  ')
	#model.stop_game(game_id1)
	'''
