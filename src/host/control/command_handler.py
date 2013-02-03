from control.load.load_config import Config_Player, Config_Args
from control.game_logic.play import Play_Args

import util

from pyplib.host_client import *
from pyplib.communication import get_request_type
from pyplib.xml_parser import parse_xml,parse_string,parse_int

from pyplib.xml_parser import XML_Parser_Error
from model.errors import Game_Action_Error
from model.errors import Model_Error

def handle(request,model):
	try:
		ele = parse_xml(request)
		#print ele.toprettyxml()
		command = parse_string(ele,'command')
		request_type = get_request_type(command)
		if request_type == 'sys':
			if command == 'test':
				version = parse_int(ele,'version')
				return respond_test(model.version)
			elif command == 'exit':
				return respond_exit()
		elif request_type == 'meta':
			if command == 'new':
				p1_uid = parse_int(ele,'p1_uid')
				p1_did = parse_int(ele,'p1_did')
				p2_uid = parse_int(ele,'p2_uid')
				p2_did = parse_int(ele,'p2_did')
				game_id = model.start_game(Config_Args(
					Config_Player(p1_uid,p1_did),
					Config_Player(p2_uid,p2_did)))
				return respond_action(command,game_id,model.out(game_id,p1_uid))
		elif request_type == 'perform':
			game_id = parse_int(ele,'game_id')
			game = model.get_game_from_id(game_id)
			player_id = parse_int(ele,'player_id')
			if command == 'setup':
				game.setup()
				return respond_action(command,game_id,model.out(game_id,player_id))
			elif command == 'draw':
				game.draw(player_id)
				return respond_action(command,game_id,model.out(game_id,player_id))
			elif command == 'play':
				game.play(Play_Args(
					game=game,
					src_uid=player_id,
					src_list=parse_int(ele,'src_list'),
					src_card=parse_int(ele,'src_card'),
					tgt_uid=parse_int(ele,'target_uid'),
					tgt_card=parse_int(ele,'target_list'),
					tgt_list=parse_int(ele,'target_card')))
				return respond_action(command,game_id,model.out(game_id,player_id))
			elif command == 'phase':
				game.step_phase()
				return respond_action(command,game_id,model.out(game_id,player_id))
			elif command == 'turn':
				game.toggle_turn()
				return respond_action(command,game_id,model.out(game_id,player_id))
			elif command == 'out':
				return respond_action(command,game_id,model.out(game_id,player_id))
			else:
				return respond_bad_action('congrats_finding_a_bug',command)
		else:
			return respond_bad_action('unknown_action',command)
	except XML_Parser_Error as e:
		util.logger.warn('Recieved bad xml: '+str(e))
		return respond_error_caught('bad_xml_request',str(e))
	except Game_Action_Error as e:
		util.logger.warn('Invalid game action: '+str(e))
		return respond_error_caught('invalid_game_action',str(e))
	except Model_Error as e:
		util.logger.warn('Invalid Model operation: '+str(e))
		return respond_error_caught('invalid_model_operation',str(e))
