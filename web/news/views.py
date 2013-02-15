from django.shortcuts import render_to_response
#from django.http import HttpResponse

def current_news(request):
	return render_to_response('current_news.html')
