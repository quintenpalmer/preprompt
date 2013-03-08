from model.play import Play_Args
from control.lstructs import Config_Player, Config_Args
from control.game_manipulator import Manipulator
from pyplib.xml_parser import parse_xml,parse_string,parse_int
from pyplib.errors import PP_Load_Error,PP_Game_Action_Error,PP_Model_Error,XML_Parser_Error,PP_Database_Error
from pyplib.host_client import *
from pyplib import database,util

def handle(request,model):
	try:
		ele = parse_xml(request)
		command = parse_string(ele,'command')
		request_type = get_request_type(command)
		if request_type == 'sys':
			if command == 'test':
				version = parse_int(ele,'version')
				ret =  respond_test(model.version)
			elif command == 'exit':
				ret =  respond_exit()
		elif request_type == 'meta':
			if command == 'new':
				p1_uid = parse_int(ele,'p1_uid')
				p1_did = parse_int(ele,'p1_did')
				p2_uid = parse_int(ele,'p2_uid')
				p2_did = parse_int(ele,'p2_did')
				if len(model.get_games_from_uid(p1_uid)) > 10:
					raise PP_Model_Error("player "+str(p1_uid)+" cannot start anymore games")
				game_id = model.start_game(Config_Args(
					Config_Player(p1_uid,p1_did),
					Config_Player(p2_uid,p2_did)))
				ret =  respond_action(command,game_id,model.out(game_id,p1_uid))
			elif command == 'list':
				uid = parse_int(ele,'uid')
				ret = respond_list(model.get_games_from_uid(uid))
		elif request_type == 'perform':
			game_id = parse_int(ele,'game_id')
			game = model.get_game_from_id(game_id)
			player_id = parse_int(ele,'player_id')
			manipulator = Manipulator(game)
			if command == 'setup':
				manipulator.setup()
				ret =  respond_action(command,game_id,model.out(game_id,player_id))
			elif command == 'draw':
				manipulator.draw(player_id)
				ret =  respond_action(command,game_id,model.out(game_id,player_id))
			elif command == 'play':
				manipulator.play(Play_Args(
					game=game,
					src_uid=player_id,
					src_list=parse_int(ele,'src_list'),
					src_card=parse_int(ele,'src_card'),
					tgt_uid=parse_int(ele,'target_uid'),
					tgt_card=parse_int(ele,'target_list'),
					tgt_list=parse_int(ele,'target_card')))
				ret =  respond_action(command,game_id,model.out(game_id,player_id))
			elif command == 'phase':
				manipulator.step_phase(player_id)
				ret =  respond_action(command,game_id,model.out(game_id,player_id))
			elif command == 'turn':
				manipulator.toggle_turn(player_id)
				ret =  respond_action(command,game_id,model.out(game_id,player_id))
			elif command == 'out':
				ret =  respond_action(command,game_id,model.out(game_id,player_id))
			else:
				ret = respond_bad_action('congrats_on_finding_a_bug',command)
			try:
				database.update('play_games','game_xml',game.xml_output(0),str,(('game_id',game_id),))
			except PP_Database_Error:
				util.logger.error("Error writing game data")
				raise PP_Load_Error("Database Column %s could not be opened"%str(game_id))
		else:
			ret =  respond_bad_action('unknown_action',command)
		return ret
	except XML_Parser_Error as e:
		util.logger.warn('Recieved bad xml: '+str(e))
		return respond_error_caught('bad_xml_request',str(e))
	except PP_Game_Action_Error as e:
		util.logger.warn('Invalid game action: '+str(e))
		return respond_error_caught('invalid_game_action',str(e))
	except PP_Model_Error as e:
		util.logger.warn('Invalid Model operation: '+str(e))
		return respond_error_caught('invalid_model_operation',str(e))
	except PP_Load_Error as e:
		util.logger.warn('Load Error: '+str(e))
		return respond_error_caught('too_few_cards_in_deck',str(e))

def get_request_type(command):
	if command in ('new','list'):
		return 'meta'
	elif command in ('setup','draw','phase','turn','play','out'):
		return 'perform'
	elif command in ('exit','test'):
		return 'sys'
	else:
		return 'unknown'
