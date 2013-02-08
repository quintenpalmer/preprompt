from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

from page_builder import build_full_page
from request_handler import handle_request
import os

from subprocess import check_output,CalledProcessError

def simple_app(environ,start_response):
	try:
		request_body_size = int(environ.get('CONTENT_LENGTH',0))
	except ValueError:
		request_body_size = 0

	html = build_full_page()

	requested_path = environ['PATH_INFO'].lstrip('/')
	if requested_path != '':
		if requested_path in os.listdir('.'):
			status = '200 OK'
			headers = [('Content-Type','text/css',)]
			f = open(requested_path,'rb')
			resp_body = f.read()
			f.close()
		else:
			status = '404 PAGENOTFOUND'
			headers = [('Content-Type','text/html'),]
			resp_body = 'Page not found, WHOOPS'
	else:
		request_body = environ['wsgi.input'].read(request_body_size)
		posts = parse_qs(request_body)
		command = posts.get('command',[''])[0]

		output = escape(handle_request(command))

		resp_body = html%(output)
		status = '200 OK'
		headers = [('Content-Type','text/html'),('Content-Length',str(len(resp_body)))]

	start_response(status,headers)
	return [resp_body]

port = 8080
httpd = make_server('',port,simple_app)
print "Serving on %s...",str(port)
httpd.serve_forever()
