from src.control.load.database_reader import Config_Player, Config_Args
from src.control.game_logic.play import Play_Args
from src.control.serializer import serialize
from pyplib.xml_parser import parse_xml,parse_string,parse_int,XML_Parser_Error
from src.model.game import Game_Action_Error
from src.model.model import Model_Error
from pyplib.communication import command_mapping
from src import util

def handle(request,model):
	try:
		ele = parse_xml(request)
		#print ele.toprettyxml()
		command = parse_string(ele,'command')
		request_type = command_mapping[command]
		if request_type == 'meta':
			if command == 'new':
				p1_uid = parse_int(ele,'p1_uid')
				p1_did = parse_int(ele,'p1_did')
				p2_uid = parse_int(ele,'p2_uid')
				p2_did = parse_int(ele,'p2_did')
				game_id = model.start_game(Config_Args(
					Config_Player(p1_uid,p1_did),
					Config_Player(p2_uid,p2_did)))
				return serialize(['ok',command,str(game_id),model.out(game_id,p1_uid)])
		elif request_type == 'sys':
			if command == 'test':
				return serialize(['ok',command,'0'])
			elif command == 'exit':
				return serialize(['ok',command,'exit'])
		elif request_type == 'perform':
			game_id = parse_int(ele,'game_id')
			game = model.get_game_from_id(game_id)
			player_id = parse_int(ele,'player_id')
			if command == 'setup':
				game.setup()
				return serialize(['ok','setup',str(game_id),model.out(game_id,player_id)])
			elif command == 'draw':
				game.draw(player_id)
				return serialize(['ok','draw',str(game_id),model.out(game_id,player_id)])
			elif command == 'play':
				game.play(Play_Args(
					game=game,
					src_uid=player_id,
					src_list=parse_int(ele,'src_list'),
					src_card=parse_int(ele,'src_card'),
					tgt_uid=parse_int(ele,'target_uid'),
					tgt_card=parse_int(ele,'target_list'),
					tgt_list=parse_int(ele,'target_card')))
				return serialize(['ok',command,str(game_id),model.out(game_id,player_id)])
			elif command == 'phase':
				game.step_phase()
				return serialize(['ok',command,str(game_id),model.out(game_id,player_id)])
			elif command == 'turn':
				game.toggle_turn()
				return serialize(['ok',command,str(game_id),model.out(game_id,player_id)])
			elif command == 'out':
				return serialize(['ok',command,str(game_id),model.out(game_id,player_id)])
			else:
				return serialize(['no_such_perform_action',command])
		else:
			return serialize(['no_such_command_type',request_type])
	except XML_Parser_Error as e:
		util.logger.warn('Recieved bad xml: '+str(e))
		return serialize(['bad_xml_request',str(e)])
	except Game_Action_Error as e:
		util.logger.warn('Invalid game action: '+str(e))
		return serialize(['invalid_game_action',str(e)])
	except Model_Error as e:
		util.logger.warn('Invalid Model operation: '+str(e))
		return serialize(['invalid_model_operation',str(e)])
