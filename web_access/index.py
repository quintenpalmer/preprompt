from wsgiref.simple_server import make_server
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import uuid

from pprint import pprint
from page_builder import gen_head, gen_not_found
from requested_paths import is_requesting_path, get_requested_path
from Cookie import SmartCookie
import util
import os

from subprocess import check_output,CalledProcessError

def simple_app(environ,start_response):
	def gen_404():
		headers.append(('Content-Type','text/html'))
		return '404 Not Found', headers,head%gen_not_found()
	requested_path = environ['PATH_INFO'].lstrip('/').split('/')

	head = gen_head(requested_path)
	status = '200 OK'
	cookie = SmartCookie()
	current_time = ('Date',format_date_time(mktime(datetime.now().timetuple())))
	headers = [current_time]

	requested_root = requested_path[0]
	file_type = requested_path[-1].split('.')[-1]
	print file_type
	#print file_type
	#print requested_path
	if '..' in requested_path or file_type not in ('about','play','game','account','login','register','','png','css'):
		status,headers,html = gen_404()
		util.logger.info('request for .. or .py page: %s',os.path.join(*requested_path))
	elif is_requesting_path(requested_path):
		status,headers,html = get_requested_path(requested_path,environ)
		html = head%html
	elif requested_root in ('css','images'):
		try:
			status = '200 OK'
			last_modified = format_date_time(os.path.getmtime(os.path.join(*requested_path)))
			#print last_modified
			if file_type == 'png':
				headers = [('Content-Type','image/png'),
							('Last-Modified',last_modified),
							current_time]
							#('Connection','Keep-Alive')]
							#('Keep-Alive','timeout=2')],'max=200')]
			elif file_type == 'css':
				headers = [('Content-Type','text/css')]
							#('Connection','Keep-Alive'),
							#('Keep-Alive','timeout=2')]#,'max=200')]
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
