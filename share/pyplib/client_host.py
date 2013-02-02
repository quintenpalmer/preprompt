import socket
from pyplib.data_types import *
host = 'localhost'
port = 52690

def send_request(request):
	s = socket.socket()
	s.connect((host,port))
	s.send(request)
	response = s.recv(16384)
	#print request
	#print response
	s.close()
	return response

def request_test(version):
	request = '<request>'
	request += '<command>test</command>'
	request += '<version>'+str(version)+'</version>'
	request += '</request>'
	return send_request(request)

def request_exit(exit_code):
	request = '<request>'
	request += '<command>exit</command>'
	request += '<version>'+str(exit_code)+'</version>'
	request += '</request>'
	return send_request(request)

def request_new(p1_uid,p1_did,p2_uid,p2_did):
	request = '<request>'
	request += '<command>new</command>'
	request += '<p1_uid>'+str(p1_uid)+'</p1_uid>'
	request += '<p1_did>'+str(p1_did)+'</p1_did>'
	request += '<p2_uid>'+str(p2_uid)+'</p2_uid>'
	request += '<p2_did>'+str(p2_did)+'</p2_did>'
	request += '</request>'
	return send_request(request)

def request_setup(game_id,player_id):
	request = '<request>'
	request += '<command>setup</command>'
	request += '<game_id>'+str(game_id)+'</game_id>'
	request += '<player_id>'+str(player_id)+'</player_id>'
	request += '</request>'
	return send_request(request)

def request_draw(game_id,player_id):
	request = '<request>'
	request += '<command>draw</command>'
	request += '<game_id>'+str(game_id)+'</game_id>'
	request += '<player_id>'+str(player_id)+'</player_id>'
	request += '</request>'
	return send_request(request)

def request_phase(game_id,player_id):
	request = '<request>'
	request += '<command>phase</command>'
	request += '<game_id>'+str(game_id)+'</game_id>'
	request += '<player_id>'+str(player_id)+'</player_id>'
	request += '</request>'
	return send_request(request)

def request_turn(game_id,player_id):
	request = '<request>'
	request += '<command>turn</command>'
	request += '<game_id>'+str(game_id)+'</game_id>'
	request += '<player_id>'+str(player_id)+'</player_id>'
	request += '</request>'
	return send_request(request)

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
