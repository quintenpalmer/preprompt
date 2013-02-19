from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
#from django.http import HttpResponse

def splash(request):
	return render_to_response('game/game.html')

@login_required
def play(request):
	print dir(request.session)
	return render_to_response('game/play.html')

@login_required
def manage(request):
	return render_to_response('game/manage.html')
