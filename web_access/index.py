from wsgiref.simple_server import make_server

from pprint import pprint
from page_builder import gen_head, gen_dummy, gen_not_found
from requested_paths import is_requesting_path, get_requested_path
from Cookie import SmartCookie
import util
import os

from subprocess import check_output,CalledProcessError

def simple_app(environ,start_response):
	def gen_404():
		return '404 NotFound', [('Content-Type','text/html')],head%gen_not_found()
	requested_path = environ['PATH_INFO'].strip('/').split('/')

	head = gen_head(requested_path)
	html = head%gen_dummy()
	status = '200 OK'
	cookie = SmartCookie()
	uid = '0'
	headers = [('Content-Type','text/html')]

	requested_root = requested_path[0]
	#print requested_path
	if '..' in requested_path or '.py' == requested_path[-1][-3:] or '.scr' == requested_path[-1][-3:]:
		status,headers,html = gen_404()
		util.logger.info('request for .. or .py page: %s',os.path.join(*requested_path))
	elif is_requesting_path(requested_path):
		status,headers,html = get_requested_path(requested_path,environ)
		html = head%html
	elif requested_root in ('css','images'):
		try:
			status = '200 OK'
			headers = [('Content-Type','text/plain')]
			f = open(os.path.join(*requested_path),'rb')
			util.logger.info('specific web page requested')
			html = f.read()
			f.close()
		except IOError:
			status,headers,html = gen_404()
			util.logger.info('request for non-existant css/image : %s',os.path.join(*requested_path))
	else:
		status,headers,html = gen_404()
		util.logger.info('request for non-existant page: %s',os.path.join(*requested_path))

	#print headers
	start_response(status,headers)
	return [html]

port = 8080
util.make_logger()
httpd = make_server('',port,simple_app)
print "Serving on %s...",str(port)
httpd.serve_forever()
