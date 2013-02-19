from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
#from django.http import HttpResponse

@login_required
def profile(request):
	return render_to_response('account/profile.html')

def require_login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('account/require_login.html',c)

def login_user(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
		print username,password
		user = authenticate(username=username,password=password)
		if user != None:
			if user.is_active:
				login(request,user)
				return render_to_response('account/profile.html')
			else:
				return account_error('Invalid credentials')
		else:
			return account_error('Invalid user')
	except KeyError:
		return account_error('Did not supply enough fields')

def register_user(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
		password_verify = request.POST['password_verify']
		email = request.POST['email']
		validate_email(email)
		if password == password_verify:
			if len(User.objects.filter(username=username)) == 0:
				User.objects.create_user(username,email,password)
				return render_to_response('account/create.html',{'username':username})
			else:
				return nccount_error('Username already exists')
		else:
			return account_error('Passwords did not match')
	except KeyError:
		return account_error('Did not supply enough fields')
	except ValidationError:
		return account_error('Email must be of format email_name@domain.xxx')

def account_error(error_text):
	return render_to_response('account/error.html',{'error_message':error_text})

@login_required
def logout_user(request):
	logout(request)
	return render_to_response('account/logout.html')
