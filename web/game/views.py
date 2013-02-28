from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from pyplib.client_host import *
from pyplib.xml_parser import parse_xml, parse_ints
from pyplib.model.main_model import Model

from django.contrib.auth.models import User
#from django.http import HttpResponse

def splash(request):
	return render_to_response('game/game.html')

def get_user_key(username):
	return User.objects.get(username=username).id

@login_required
def play(request):
	username = request.COOKIES['username']
	uid = get_user_key(username)
	print uid
	gids = parse_ints(parse_xml(request_list(uid)),'game_id')
	return render_to_response('game/play.html',{'game_ids':gids})

@login_required
def manage(request):
	return render_to_response('game/manage.html')

@login_required
def perform(request):
	return render_to_response('game/play.html')

@login_required
def game_view(request,game_id):
	command = request.POST
	username = request.COOKIES['username']
	uid = get_user_key(username)
	print handle_request(command.get('command'),{'game_id':game_id,'player_id':uid})
	model = Model(uid)
	model.update_game(request_out(game_id,uid))
	game = model.games[int(game_id)]
	print game
	print game.them.collection.hand.cards
	c = {}
	c.update(csrf(request))
	c['game']=game
	return render_to_response('game/game_view.html',c)

def handle_request(command,req):
	if req.has_key('player_id'):
		player_id = req['player_id']
	if req.has_key('game_id'):
		game_id = req['game_id']
	if command != None:
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
	else:
		return "Enter a Command"
