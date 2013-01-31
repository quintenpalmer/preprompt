from src.control.load.database_reader import Config_Player, Config_Args
from src.control.game_logic.play import Play_Args
from src.control.serializer import serialize

def handle(request,model):
	request = request.split(' ')
	#print request
	command = request.pop(0)
	if command == 'test':
		return serialize(['ok'])
	elif command == 'exit':
		return serialize(['done'])
	elif command == 'new':
		game_id = model.start_game(Config_Args(Config_Player(request[0],request[1]),Config_Player(request[2],request[3])))
		return serialize(['new_game',str(game_id),model.out(game_id,request[0])])
	else:
		game_id = int(request.pop(0))
		game = model.get_game_from_id(game_id)
		src_uid = request.pop(0)
		if command == 'setup':
			game.setup()
		elif command == 'draw':
			game.draw(src_uid)
		elif command == 'play':
			game.play(Play_Args(
				game=game,
				src_uid=src_uid,
				src_list=int(request.pop(0)),
				src_card=int(request.pop(0)),
				tgt_uid=int(request.pop(0)),
				tgt_card=int(request.pop(0)),
				tgt_list=int(request.pop(0))))
		elif command == 'phase':
			game.step_phase()
		elif command == 'turn':
			game.toggle_turn()
		elif command == 'out':
			return serialize(['xml',str(game_id),model.out(game_id,src_uid)])
			pass
		else:
			return serialize(['no_such_command'])
		return serialize(['ok',])
