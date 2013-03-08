from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from pyplib.client_host import *
from pyplib.xml_parser import parse_xml, parse_ints
from pyplib.model.main_model import Model
from pyplib import database
from django.http import HttpResponse

def splash(request):
	return render_to_response('play/splash.html')

def get_user_key(username):
	return User.objects.get(username=username).id

@login_required
def ajax_new_game(request):
	command = request.POST
	uid = get_user_key(request.COOKIES['username'])
	if command.get('command') == 'new':
		print handle_request('new',{'player_id':uid})
	gids = sorted(parse_ints(parse_xml(request_list(uid)),'game_id'))
	return HttpResponse(str(gids).replace(' ','').strip('[').strip(']'),content_type='text/plain')

@login_required
def games(request):
	command = request.POST
	uid = get_user_key(request.COOKIES['username'])
	if command.get('command') == 'new':
		print handle_request('new',{'player_id':uid})
	gids = sorted(parse_ints(parse_xml(request_list(uid)),'game_id'))
	c = {}
	c.update(csrf(request))
	c['game_ids']=str(gids).replace(' ','').strip('[').strip(']')
	print c['game_ids']
	return render_to_response('play/games.html',c)

@login_required
def perform(request):
	return render_to_response('play/games.html')

@login_required
def game(request,game_id):
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
	return render_to_response('play/game.html',c)


@login_required
def manage(request):
	return render_to_response('play/manage.html')

@login_required
def cards(request):
	uid = get_user_key(request.COOKIES['username'])
	cards = database.select('play_cards','card_name_id',where=('uid='+str(uid),))
	cards = create_sub_lists(cards,5)
	return render_to_response('play/cards.html',{'cards':cards})

@login_required
def deck(request,deck):
	command = request.POST
	uid = str(get_user_key(request.COOKIES['username']))
	deck_contents = command.get('deck')
	if command.has_key('deck'):
		database.delete('play_decks',where=(('uid='+uid),('deck_id='+deck)))
		if deck_contents != '':
			for card in deck_contents.split(','):
				database.insert('play_decks',(int,int,int,int),(None,uid,deck,card))
	in_deck = database.select('play_decks','card_id',where=(('uid='+uid),('deck_id='+deck)))
	for i in range(len(in_deck)):
		in_deck_card = in_deck[i]
		in_deck[i] = (database.select('play_cards','card_name_id',where=(('uid='+str(uid)),('id='+str(in_deck_card))))[0],in_deck[i])
	out_deck = database.select('play_cards','card_name_id,id',where=(('uid='+str(uid)),))
	out_deck = [out_deck_card for out_deck_card in out_deck if out_deck_card[1] not in [in_deck_card[1] for in_deck_card in in_deck]]
	#cards = create_sub_lists(cards,5)
	in_deck = ','.join([str(card).replace(', ','_').strip('(').strip(')') for card in in_deck])
	out_deck = ','.join([str(card).replace(', ','_').strip('(').strip(')') for card in out_deck])
	c = {}
	c.update(csrf(request))
	c['deck'] = deck
	c['in_deck'] = in_deck
	c['out_deck'] = out_deck
	return render_to_response('play/deck.html',c)

@login_required
def deck_new(request):
	uid = get_user_key(request.COOKIES['username'])
	decks = sorted(database.select('play_decks','deck_id',where=('uid='+str(uid),)))
	if len(decks) != 0:
		deck_id = str(int(decks[-1])+1)
	else:
		deck_id = 0
	return deck(request,deck_id)

@login_required
def decks(request):
	uid = get_user_key(request.COOKIES['username'])
	decks = list(set(database.select('play_decks','deck_id',where=('uid='+str(uid),))))
	decks = create_sub_lists(decks,3)
	return render_to_response('play/decks.html',{'decks':decks})

def create_sub_lists(my_list,sub_list_size):
	return [my_list[i:i+sub_list_size] for i in range(0,len(my_list), sub_list_size)]

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
			p2_uid = 2
			p2_did = 0
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
