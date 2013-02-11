from page_builder import *
from cgi import parse_qs, escape
from command_handler import handle_request
from hashlib import md5
import Cookie
import util
import os

def is_requesting_path(url):
	return url[0] in ('','game','about','account')

def get_requested_path(requested_path,environ):
	try:
		request_body_size = int(environ.get('CONTENT_LENGTH',0))
	except ValueError:
		request_body_size = 0
	def get_next(path):
		try:
			return path.pop(0)
		except IndexError:
			return ''
	status = '200 OK'
	headers = [('Content-Type','text/html')]
	requested_root = requested_path.pop(0)
	request_body = environ['wsgi.input'].read(request_body_size)
	posts = parse_qs(request_body)
	try:
		cookies = environ['HTTP_COOKIE']
		logged_in = True
		cookies = [cookie.split('=') for cookie in cookies.split(';')]
		uname = 'you'
		try:
			for cookie in cookies:
				if cookie[0] == 'uname':
					uname = cookie[1]
			if uname == 'you':
				logged_in = False
		except IndexError:
			logged_in = False
	except KeyError:
		logged_in = False
	html = ''
	if requested_root == '':
		html = gen_home()
	elif requested_root == 'game':
		sub_path = get_next(requested_path)
		if sub_path == '':
			if logged_in:
				html = gen_game_splash()
			else:
				html = gen_req_login()
		elif sub_path == 'play':
			command = posts.get('command',[''])[0]
			output = escape(handle_request(command))
			util.logger.info('%s processed'%command)
			html = gen_game()%output
		else:
			html = gen_not_found()
	elif requested_root == 'about':
		html = gen_about()
	elif requested_root == 'account':
		sub_path = get_next(requested_path)
		if sub_path == '':
			if logged_in:
				html = gen_account()%uname
			else:
				html = gen_login()
				html += gen_register()
		elif sub_path == 'login':
			uname = posts.get('luname',[''])[0]
			password = posts.get('lpass',[''])[0]
			path = os.path.join(os.environ['pyp'],'root','opt','postprompt','tables','credentials')
			file_path = os.path.join(path,uname+'.stable')
			try:
				if uname+'.stable' in os.listdir(path):
					f = open(file_path,'rb')
					passhash = f.readlines()[0]
					if md5(password).digest() == passhash:
						headers.append(('Set-Cookie','uname='+uname+'; path=/'))
						html = gen_welcome()%uname
					else:
						html = gen_improper_login()%uname
				else:
					html = gen_improper_login()%uname
			except IOError:
				status = '500 Internal Error'
				html = gen_internal_error()
		elif sub_path == 'register':
			uname = posts.get('runame',[''])[0]
			password = posts.get('rpass',[''])[0]
			password_verify = posts.get('rpass2',[''])[0]
			nickname = posts.get('rnickname',[''])[0]
			if password != password_verify:
				html = gen_password_mismatch()
			else:
				path = os.path.join(os.environ['pyp'],'root','opt','postprompt','tables','credentials',uname+'.stable')
				if os.path.exists(path):
					html = gen_username_exists()%uname
				else:
					try:
						f = open(path,'w')
						f.write(md5(password).digest())
						f.close()
						html = gen_success_account()%uname
					except IOError:
						status = '500 Internal Error'
						html = gen_internal_error()
		else:
			html = gen_not_found()
	return status,headers,html
