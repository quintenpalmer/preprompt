from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.conf import settings
import datetime
#from django.http import HttpResponse

from pyplib import database


@login_required
def profile(request):
	return render_to_response('account/profile.html')

def require_login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('account/require_login.html',c)

def set_cookie(response,key,value,days_expire=3):
	max_age = days_expire * 24 * 60 * 60
	expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
	response.set_cookie(key,value,max_age=max_age,expires=expires,domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE)

def login_user(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user != None:
			if user.is_active:
				login(request,user)
				response = render_to_response('account/profile.html')
				set_cookie(response,'username',username)
				return response
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
				register_add_cards(username)
				return render_to_response('account/create.html',{'username':username})
			else:
				return account_error('Username already exists')
		else:
			return account_error('Passwords did not match')
	except KeyError:
		return account_error('Did not supply enough fields')
	except ValidationError:
		return account_error('Email must be of format email_name@domain.xxx')

def account_error(error_text):
	return render_to_response('account/error.html',{'error_message':error_text})

def register_add_cards(username):
	print database.select('auth_user','id',where=("username='"+username+"'",))
	uid = int(database.select('auth_user','id',where=("username='"+username+"'",))[0])
	values_list = []
	for i in range(100):
		values_list.append((None,0,uid))
	database.insert_batch('game_cards',(int,int,int),values_list)

@login_required
def logout_user(request):
	logout(request)
	return render_to_response('account/logout.html')
