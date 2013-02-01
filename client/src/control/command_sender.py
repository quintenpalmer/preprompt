
from pyplib.communication import generate_request,command_mapping
from src.control.network import send_request
from src.view.game_drawer import draw_game

def build_and_send_and_process_request(command,model,params=[]):
	super_command = command_mapping[command]
	resp = send_request(generate_request(command,model,params))
	if super_command == 'meta':
		model.add_game(resp)
		draw_game(model.get_current_game())
	elif super_command == 'perform':
		out = send_request(generate_request('out',model))
		model.update_game(out)
		draw_game(model.get_current_game())
	elif super_command == 'sys':
		pass
	return resp
