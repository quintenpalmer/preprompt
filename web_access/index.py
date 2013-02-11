from wsgiref.simple_server import make_server
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime,ctime,asctime,localtime
import uuid

from page_builder import gen_head, gen_not_found
from requested_paths import is_requesting_path, get_requested_path
from Cookie import SmartCookie
import util
import os

from subprocess import check_output,CalledProcessError

def simple_app(environ,start_response):
	def gen_404():
		status = '404 Not Found'
		headers.append(('Content-Type','text/html'))
		html = head%gen_not_found()
	def valid_filetype(path):
		if '.' in requested_path[-1]:
			if not requested_path[-1].split('.')[-1] in ('png','css','ico','ttf'):
				return False
		return True

	current_time = ('Date',format_date_time(mktime(datetime.now().timetuple())))
	requested_path = environ['PATH_INFO'].lstrip('/').split('/')
	head = gen_head(requested_path)
	status = '500 Internal Error'
	html = '500 - Internal Error'
	headers = [current_time]
	requested_root = requested_path[0]

	if '..' in requested_path or not valid_filetype(requested_path):
		gen_404()
		util.logger.info('request for .. or invalid file type: %s',os.path.join(*requested_path))
	elif is_requesting_path(requested_path):
		status,headers,html = get_requested_path(requested_path,environ)
		html = head%html
	elif requested_root in ('css','images','fonts'):
		filename = os.path.join(*requested_path)
		try:
			status = '200 OK'
			last_modified = format_date_time(os.path.getmtime(filename))
			print ctime(os.path.getmtime(filename))
			print asctime(localtime(os.path.getmtime(filename)))
			print os.path.getmtime(filename)
			print last_modified
			file_type = requested_path[-1].split('.')[-1]
			if file_type == 'png' or file_type == 'ico':
				headers.append(('Content-Type','image/png'))
			elif file_type == 'css':
				headers.append(('Content-Type','text/css'))
			elif file_type == 'ttf':
				headers.append(('Content-Type','text/plain'))
			headers.append(('Last-Modified',last_modified))
			headers.append(('ETag',str(uuid.uuid3(uuid.NAMESPACE_DNS,filename))))
			#('Connection','Keep-Alive'),
			#('Keep-Alive','timeout=2')]#,'max=200')]
			f = open(filename,'rb')
			util.logger.info('specific web page requested')
			html = f.read()
			f.close()
		except IOError:
			gen_404()
			util.logger.info('request for non-existant css/image : %s',os.path.join(*requested_path))
	else:
		gen_404()
		util.logger.info('request for non-existant page: %s',os.path.join(*requested_path))

	start_response(status,headers)
	return [html]

port = 8080
util.make_logger()
httpd = make_server('',port,simple_app)
print "Serving on %s...",str(port)
httpd.serve_forever()
