from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

from subprocess import check_output,CalledProcessError

def parse_request(request):
	try:
		command = request.split(' ')[0]
	except IndexError:
		command = ''
	try:
		if command == 'ls':
			to_run = ['ls',request[2:].strip() or '.']
			return check_output(to_run)
		elif command == 'cat':
			to_run = ['cat',request[3:].strip() or '.']
			return check_output(to_run)
		else:
			return 'not a valid command'
	except CalledProcessError:
		return 'error running command'

html = """<html>
<head>
<link href="css.css" rel="stylesheet" type="text/css">
<title>PostPrompt - Game</title>
</head>
<body>
	<h1>
	Welcome to PostPrompt
	</h1>
	<form method="post">
		<p>
			Enter a command: <input type="text" name="command">
		</p>
		<p>
			<input type="submit" value="Run">
		</p>
	</form>
	<p>
		Output:
	</p>
	<div id="output">
%s
	</div>
</body>
</html>
"""

def simple_app(environ,start_response):
	try:
		request_body_size = int(environ.get('CONTENT_LENGTH',0))
	except ValueError:
		request_body_size = 0

	if environ['PATH_INFO'] != '/':
		if environ['PATH_INFO'] == '/css.css':
			status = '200 OK'
			headers = [('Content-Type','text/css',)]
			f = open('css.css')
			resp_body = f.read()
			f.close()
		else:
			status = '404 NOTFOUND'
			headers = [('Content-Type','text/html'),]
			resp_body = 'Page not found, WHOOPS'
	else:
		request_body = environ['wsgi.input'].read(request_body_size)
		posts = parse_qs(request_body)
		command = posts.get('command',[''])[0]

		output = parse_request(command).strip()

		resp_body = html%(output)
		status = '200 OK'
		headers = [('Content-Type','text/html'),('Content-Length',str(len(resp_body)))]

	start_response(status,headers)
	return [resp_body]

port = 8080
httpd = make_server('',port,simple_app)
print "Serving on %s...",str(port)
httpd.serve_forever()
