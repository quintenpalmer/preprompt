from pyplib.client_host import *

def handle_request(command):
	command = command.lower()
	if command == 'test':
		return request_test(0)
	elif command == 'exit':
		return request_exit(0)
	elif command == 'new':
		p1_uid = 26
		p1_did = 0
		p2_uid = 13
		p2_did = 1
		return request_new(p1_uid,p1_did,p2_uid,p2_did)
	else:
		game_id = 0
		player_id = 26
		if command == 'setup':
			return request_setup(game_id,player_id)
		elif command == 'draw':
			return request_draw(game_id,player_id)
		elif command == 'phase':
			return request_phase(game_id,player_id)
		elif command == 'turn':
			return request_turn(game_id,player_id)
		elif command == 'out':
			return request_out(game_id,player_id)
		elif command == 'list':
			return request_list()
		elif command == 'play':
			src_list = 1
			src_card = 0
			target_uid = 13
			target_list = 2
			target_card = 0
			return request_play(game_id,player_id,src_list,src_card,target_uid,target_list,target_card)
		else:
			return "Not a valid command"
	
def linux_time(request):
	try:
		command = request.split(' ')[0]
	except IndexError:
		command = ''
	try:
		if command == 'ls':
			to_run = ['ls',request[2:].strip() or '.']
			return check_output(to_run)
		elif command == 'cat':
			to_run = ['cat',request[3:].strip() or '.']
			return check_output(to_run)
		else:
			return 'not a valid command'
	except CalledProcessError:
		return 'error running command'
