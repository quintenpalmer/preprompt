from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from pyplib.client_host import *
from pyplib.xml_parser import parse_xml, parse_ints
#from django.http import HttpResponse

def splash(request):
	return render_to_response('game/game.html')

@login_required
def play(request):
	uid = request.COOKIES['username']
	gids = parse_ints(parse_xml(request_list(uid)),'game_id')
	return render_to_response('game/play.html',{'game_ids':gids})

@login_required
def manage(request):
	return render_to_response('game/manage.html')

def perform(request):
	return render_to_response('game/play.html')

def game_view(request,game_id):
	uid = request.COOKIES['username']
	game_xml = request_out(game_id,uid)
	return render_to_response('game/game_view.html',{'game_xml':game_xml})
