from django.shortcuts import render_to_response
#from django.http import HttpResponse

def homepage(request):
	return render_to_response('homepage.html')
