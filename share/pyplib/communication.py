
def get_game_id(model,params,dummy):
	return model.current_game_id

def get_game_uid(model,params,who):
	if who == 0:
		return model.get_current_game().me.player.uid
	else:
		return model.get_current_game().them.player.uid

def get_logged_in_uid(model,params,dummy):
	return model.logged_in_uid

def get_param(model,params,index):
	return params[index]

def get_version(model,params,dummy):
	return 0

def get_exit_status(model,params,dummy):
	return 0

command_mapping = {}
command_mapping['new'] = 'meta'
command_mapping['setup'] = 'perform'
command_mapping['draw'] = 'perform'
command_mapping['phase'] = 'perform'
command_mapping['turn'] = 'perform'
command_mapping['play'] = 'perform'
command_mapping['out'] = 'perform'
command_mapping['exit'] = 'sys'
command_mapping['test'] = 'sys'

command_args = {}
command_args['new'] = (('player1_uid',get_param,0),('player1_did',get_param,1),('player2_uid',get_param,2),('player2_did',get_param,3))
command_args['setup'] = (('game_id',get_game_id,0),('player_id',get_game_uid,0))
command_args['draw'] = (('game_id',get_game_id,0),('player_id',get_game_uid,0))
command_args['phase'] = (('game_id',get_game_id,0),('player_id',get_game_uid,0))
command_args['turn'] = (('game_id',get_game_id,0),('player_id',get_game_uid,0))
command_args['play'] = (('game_id',get_game_id,0),('player_id',get_game_uid,0),('src_list',get_param,0),('src_card',get_param,1),('target_uid',get_param,2),('target_list',get_param,3),('target_card',get_param,4))
command_args['exit'] = (('exit_status',get_exit_status,0),)
command_args['test'] = (('version',get_version,0),)
command_args['out'] = (('game_id',get_game_id,0),('player_id',get_logged_in_uid,0))

def generate_request(command,model,params=[]):
	request = '<request>'
	request += '<request_type>' + command_mapping[command] + '</request_type>'
	request += '<command>' + command + '</command>'
	args = command_args[command]
	for arg in args:
		tag = arg[0]
		func = arg[1]
		func_params = arg[2]
		request += '<' + tag + '>' + str(func(model,params,func_params)) + '</' + tag + '>'
	request += '</request>'
	return request
