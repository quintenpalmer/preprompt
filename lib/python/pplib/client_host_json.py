import socket

import json

host = 'localhost'
port = 52690

def send_request(request):
	s = socket.socket()
	s.connect((host,port))
	s.send(request)
	response = s.recv(32768).rstrip()
	#print request
	#print response
	with open('tmp.json','w') as f:
		f.write(response)
	s.close()
	return response

def request_test(version):
	return send_request(json.dumps( { 'request' : { 'command' : 'test', 'version' : str(version) } } ) )

def request_exit(exit_code):
	return send_request(json.dumps( { 'request' : { 'command' : 'exit', 'version' : str(exit_code) } } ) )

def request_close(close_code):
	return send_request(json.dumps( { 'request' : { 'command' : 'close', 'version' : str(close_code) } } ) )

def request_list(uid):
	return send_request(json.dumps( { 'request' : { 'command' : 'list', 'uid' : str(uid) } } ) )

def request_new(p1_uid,p1_did,p2_uid,p2_did):
	return send_request(json.dumps( { 'request' : { 'command' : 'new',
		'p1_uid' : str(p1_uid),
		'p1_did' : str(p1_did),
		'p2_uid' : str(p2_uid),
		'p2_did' : str(p2_did),
	} } ) )

def request_setup(game_id,player_id):
	return send_request(json.dumps( { 'request' : { 'command' : 'setup', 'gameId' : str(game_id) , 'playerId' : str(player_id) } } ) )

def request_draw(game_id,player_id):
	return send_request(json.dumps( { 'request' : { 'command' : 'draw', 'gameId' : str(game_id) , 'playerId' : str(player_id) } } ) )

def request_phase(game_id,player_id):
	return send_request(json.dumps( { 'request' : { 'command' : 'phase', 'gameId' : str(game_id) , 'playerId' : str(player_id) } } ) )

def request_turn(game_id,player_id):
	return send_request(json.dumps( { 'request' : { 'command' : 'turn', 'gameId' : str(game_id) , 'playerId' : str(player_id) } } ) )

def request_play(game_id,player_id,src_list,src_card,target_uid,target_list,target_card):
	request = '<request>'
	request += '<command>play</command>'
	request += '<game_id>'+str(game_id)+'</game_id>'
	request += '<player_id>'+str(player_id)+'</player_id>'
	request += '<src_list>'+str(src_list)+'</src_list>'
	request += '<src_card>'+str(src_card)+'</src_card>'
	request += '<target_uid>'+str(target_uid)+'</target_uid>'
	request += '<target_list>'+str(target_list)+'</target_list>'
	request += '<target_card>'+str(target_card)+'</target_card>'
	request += '</request>'
	return send_request(request)

def request_out(game_id,player_id):
	request = '<request>'
	request += '<command>out</command>'
	request += '<game_id>'+str(game_id)+'</game_id>'
	request += '<player_id>'+str(player_id)+'</player_id>'
	request += '</request>'
	return send_request(request)

def request_forfeit(game_id,player_id):
	request = '<request>'
	request += '<command>forfeit</command>'
	request += '<game_id>'+str(game_id)+'</game_id>'
	request += '<player_id>'+str(player_id)+'</player_id>'
	request += '</request>'
	return send_request(request)
