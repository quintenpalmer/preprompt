from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

from page_builder import gen_head, gen_dummy, gen_not_found, gen_home, gen_game, gen_about, gen_account
from request_handler import handle_request
import util
import os

from subprocess import check_output,CalledProcessError

def simple_app(environ,start_response):
	try:
		request_body_size = int(environ.get('CONTENT_LENGTH',0))
	except ValueError:
		request_body_size = 0

	requested_path = environ['PATH_INFO'].lstrip('/')

	head = gen_head(requested_path)
	html = head%gen_dummy()
	status = '200 OK'
	headers = [('Content-Type','text/html')]

	requested_root = requested_path.split('/')[0]
	if requested_path == '':
		status = '200 OK'
		headers = [('Content-Type','text/html')]
		html = head%gen_home()
	elif requested_path == 'game':
		request_body = environ['wsgi.input'].read(request_body_size)
		posts = parse_qs(request_body)
		command = posts.get('command',[''])[0]

		output = escape(handle_request(command))

		util.logger.info('%s processed'%command)
		html = head%gen_game()%output
		status = '200 OK'
		headers = [('Content-Type','text/html'),('Content-Length',str(len(html)))]
	elif requested_path == 'about':
		status = '200 OK'
		headers = [('Content-Type','text/html')]
		html = head%gen_about()
	elif requested_path == 'account':
		status = '200 OK'
		headers = [('Content-Type','text/html')]
		html = head%gen_account()
	elif requested_path != '':
		if requested_root in os.listdir('.'):
			status = '200 OK'
			headers = [('Content-Type','text/plain')]
			f = open(requested_path,'rb')
			util.logger.info('specific web page requested')
			html = f.read()
			f.close()
		else:
			status = '404 PAGENOTFOUND'
			headers = [('Content-Type','text/html'),]
			html = head%gen_not_found()
			util.logger.info('request for non-existant page: %s',requested_path)

	start_response(status,headers)
	return [html]

port = 8080
util.make_logger()
httpd = make_server('',port,simple_app)
print "Serving on %s...",str(port)
httpd.serve_forever()
