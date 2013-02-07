import socket
from pyplib.data_types import *
host = 'localhost'
port = 52690

def respond_test(version):
	resp = '<resp>'
	resp += '<resp_status>ok</resp_status>'
	resp += '<resp_type>test</resp_type>'
	resp += '<version>'+str(version)+'</version>'
	resp += '</resp>'
	return resp

def respond_exit():
	resp = '<resp>'
	resp += '<resp_status>ok</resp_status>'
	resp += '<resp_type>exit</resp_type>'
	resp += '</resp>'
	return resp

def respond_list(model):
	resp = '<resp>'
	resp += '<resp_status>ok</resp_status>'
	resp += '<resp_type>list</resp_type>'
	for game_id in model.games.keys():
		resp += '<game_id>%s</game_id>'%str(game_id)
	resp += '</resp>'
	return resp

def respond_action(command,game_id,game_xml):
	resp = '<resp>'
	resp += '<resp_status>ok</resp_status>'
	resp += '<resp_type>'+str(command)+'</resp_type>'
	resp += '<game_id>'+str(game_id)+'</game_id>'
	resp += '<game_xml>'+str(game_xml)+'</game_xml>'
	resp += '</resp>'
	return resp

def respond_bad_action(error_id,command):
	resp = '<resp>'
	resp += '<resp_status>'+str(error_id)+'</resp_status>'
	resp += '<error_message>'+str(error_message)+'</error_message>'
	resp += '</resp>'
	return resp

def respond_error_caught(error_id,error_message):
	resp = '<resp>'
	resp += '<resp_status>'+str(error_id)+'</resp_status>'
	resp += '<error_message>'+str(error_message)+'</error_message>'
	resp += '</resp>'
	return resp
