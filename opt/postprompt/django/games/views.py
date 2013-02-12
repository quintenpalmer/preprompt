from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def index(request):
	print 'index'
	return render_to_response('wrapper.html',{'menu':'MENU','content':"Hello World!"})

def getcss(request,css_file):
	print css_file
	return render_to_response(css_file,{})
