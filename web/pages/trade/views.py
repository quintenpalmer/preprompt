from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from pplib.client_host_xml import *
from pplib.xml_parser import parse_xml, parse_ints
from pplib import database

def splash(request):
	return render_to_response('trade/splash.html')

@login_required
def cards(request):
	uid = get_user_key(request.COOKIES['username'])
	cards = database.select('play_cards','card_name_id',where=('uid='+str(uid),))
	return render_to_response('trade/cards.html',{'cards':cards})

def get_user_key(username):
	return User.objects.get(username=username).id

'''
@login_required
def play(request):
	command = request.POST
	username = request.COOKIES['username']
	uid = get_user_key(username)
	print handle_request(command.get('command'),{'player_id':uid})
	gids = sorted(parse_ints(parse_xml(request_list(uid)),'game_id'))
	c = {}
	c.update(csrf(request))
	c['game_ids']=gids
	return render_to_response('game/play.html',c)

@login_required
def manage(request):
	return render_to_response('game/manage.html')

@login_required
def deck(request,deck):
	uid = get_user_key(request.COOKIES['username'])
	cards = database.select('play_decks','card_ids',where=('uid='+str(uid,),'deck_id='+str(deck)))[0].split(',')
	return render_to_response('game/deck.html',{'deck':deck,'cards':cards})

@login_required
def deck_new(request):
	uid = get_user_key(request.COOKIES['username'])
	decks = sorted([deck_id[0] for deck_id in database.select('play_decks','deck_id',where=('uid='+str(uid),))])
	deck = str(int(decks[-1])+1)
	cards = '1,1,1,5,1,1,2,3,1,4,4,1,1,1,1,1,2,3,1,4,4,1,1,1,1,1,2,3,1,4,4,1,1,1,1,1,2,3,1,4,4'
	database.insert('play_decks',(int,int,int,str),(None,int(uid),int(deck),cards))
	return render_to_response('game/deck.html',{'deck':deck,'cards':cards})

@login_required
def decks(request):
	uid = get_user_key(request.COOKIES['username'])
	decks = [deck_id[0] for deck_id in database.select('play_decks','deck_id',where=('uid='+str(uid),))]
	return render_to_response('game/decks.html',{'decks':decks})

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
	out = request_out(game_id,uid)
	model.update_game(out)
	game = model.games[int(game_id)]
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
			p1_uid = player_id
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
'''
