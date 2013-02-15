from django.shortcuts import render_to_response
#from django.http import HttpResponse

def game_splash(request):
	return render_to_response('game.html')

def game_play(request):
	return render_to_response('game_play.html')

def game_manage(request):
	return render_to_response('game_manage.html')
