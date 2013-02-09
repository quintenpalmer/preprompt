def gen_head():
	html = """<html>
<head>
<link href="/css/site_wide.css" rel="stylesheet" type="text/css">
<title>PostPrompt - Game</title>
</head>
<body>
	<div id=top>
	<div id="logo"> 
		<a href="/">
		<span>
			<img src="/images/logos/logo.png" border=0/>
		</span>
		</a>
	</div>
	</div>
	<h1>
	Welcome to PostPrompt
	</h1>
	<div class="main">
	%s
	</div>
</body>
</html>
"""
	return html
	
def gen_content():
	html="""
	<form method="post">
		<p>
			<input type="submit" name="command" value="New">
			<input type="submit" name="command" value="Out">
			<input type="submit" name="command" value="Draw">
			<input type="submit" name="command" value="Phase">
			<input type="submit" name="command" value="Turn">
			<input type="submit" name="command" value="Setup">
		</p>
	</form>
	<p>
		Output:
	</p>
	<div id="output">
%s
	</div>
"""
	return html

def gen_dummy():
	html="""
	<p>
		This is a dummy page!
	</p>
"""
	return html

def gen_not_found():
	html="""
	<p>
		404 - Page not found
	</p>
"""
	return html
