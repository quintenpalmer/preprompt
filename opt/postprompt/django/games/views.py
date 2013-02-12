from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render_to_response('wrapper.html',{'menu':0,'content':"Welcome to Post Prompt!"})
def game(request):
	return render_to_response('wrapper.html',{'menu':0,'content':"It's Game Time!"})
def about(request):
	return render_to_response('wrapper.html',{'menu':0,'content':"I'm Quinten!"})
def account(request):
	return render_to_response('wrapper.html',{'menu':0,'content':"Login coming soon!"})

def getcss(request,css_file):
	print css_file
	return render_to_response(css_file,{})
