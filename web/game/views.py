from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from pyplib.client_host import *
from pyplib.xml_parser import parse_xml, parse_ints

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
	username = request.COOKIES['username']
	uid = get_user_key(username)
	game_xml = request_out(game_id,uid)
	return render_to_response('game/game_view.html',{'game_xml':game_xml})
