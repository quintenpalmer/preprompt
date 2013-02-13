from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render_to_response('home.html')
def game(request):
	return render_to_response('game.html')
def about(request):
	return render_to_response('about.html')
def account(request):
	return render_to_response('account.html')

#def getcss(request,css_file):
#	return render_to_response(css_file,{})
