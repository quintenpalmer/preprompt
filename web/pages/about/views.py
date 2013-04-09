from django.shortcuts import render_to_response
#from django.http import HttpResponse

def about_me(request):
	return render_to_response('about/me.html')
