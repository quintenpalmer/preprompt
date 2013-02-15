from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
#from django.http import HttpResponse

def profile(request):
	return render_to_response('account.html')

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username,password=password)
	if user != None:
		if user.is_active:
			login(request,user)
			return render_to_response('account_profile.html')
		else:
			return render_to_response('login_failed.html')
	else:
		return render_to_response('login_failed.html')

def register(request):
	username = request.POST['username']
	password = request.POST['password']
	password_verify = request.POST['password_verify']
	email = request.POST['email']
	nickname = request.POST['nickname']
	if password == password_verify:
		return render_to_response('homepage.html')
	else:
		return render_to_response('account_error',{'error_message','Passwords did not match'})

def logout(request):
	return render_to_response('account_error',{'error_message','logout not implemented'})
