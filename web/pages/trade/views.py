from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from pplib.client_host_json import *
from pplib.json_parser import PPjo
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

