from src.control.load.database_reader import Config_Player, Config_Args
from src.control.game_logic.play import Play_Args
from src.control.serializer import serialize
from pyplib.xml_parser import parse_xml,parse_string,parse_int
from pyplib.communication import command_args

def xml_handle(request,model):
	ele = parse_xml(request)
	#print ele.toprettyxml()
	super_command = parse_string(ele,'request_type')
	command = parse_string(ele,'command')
	if super_command == 'meta':
		if command == 'new':
			player1_uid = parse_int(ele,'player1_uid')
			player1_did = parse_int(ele,'player1_did')
			player2_uid = parse_int(ele,'player2_uid')
			player2_did = parse_int(ele,'player2_did')
			game_id = model.start_game(Config_Args(Config_Player(player1_uid,player1_did),Config_Player(player2_uid,player2_did)))
			print model.games
			return serialize(['ok','new_game',str(game_id),model.out(game_id,player1_uid)])
	elif super_command == 'sys':
		if command == 'test':
			return serialize(['ok','0'])
		elif command == 'exit':
			return serialize(['ok','exit'])
	elif super_command == 'perform':
		game_id = parse_int(ele,'game_id')
		game = model.get_game_from_id(game_id)
		player_id = parse_int(ele,'player_id')
		#args = parse_string(ele,'args')
		if command == 'setup':
			game.setup()
		elif command == 'draw':
			game.draw(player_id)
		elif command == 'play':
			game.play(Play_Args(
				game=game,
				src_uid=player_id,
				src_list=parse_int(ele,'src_list'),
				src_card=parse_int(ele,'src_card'),
				tgt_uid=parse_int(ele,'target_uid'),
				tgt_card=parse_int(ele,'target_list'),
				tgt_list=parse_int(ele,'target_card')))
		elif command == 'phase':
			game.step_phase()
		elif command == 'turn':
			game.toggle_turn()
		elif command == 'out':
			return serialize(['ok','xml',str(game_id),model.out(game_id,player_id)])
		else:
			return serialize(['no_such_command'])
		return serialize(['ok',])

def handle(request,model):
	return xml_handle(request,model)

def space_delim_handle(request,model):
	request = request.split(' ')
	print request
	command = request.pop(0)
	if command == 'test':
		return serialize(['ok'])
	elif command == 'exit':
		return serialize(['exit'])
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
