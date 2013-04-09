from django.shortcuts import render_to_response
#from django.http import HttpResponse

def current(request):
	return render_to_response('news/current.html')
