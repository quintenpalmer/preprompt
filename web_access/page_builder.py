def gen_head(url):
	html = """<html>
<head>
<link href="/css/sitewide.css" rel="stylesheet" type="text/css">
<link href="/images/logos/logo.ico" rel="icon" type="text/x-icon">
<link href="/images/logos/logo.ico" rel="shortcut icon" type="text/x-icon">
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
"""+gen_menu(url)+"""
	<div class="main">
	<div class="all" id="content">
	%s
	</div>
	</div>
</body>
</html>
"""
	return html

def gen_menu(url):
	url = url.split('/')[0]
	home=game=about=account=''
	if url=='':
		home='-current'
	elif url=='game':
		game='-current'
	elif url=='about':
		about='-current'
	elif url=='accont':
		account='-current'
	html="""
	</div id="menubar">
	<ul class="menu" id="menu">
	<li class="menu-home%s">
	<a href="/"><span>Home</span></a>
	</li>
	<li class="menu-game%s">
	<a href="/game"><span>Game</span></a>
	</li>
	<li class="menu-about%s">
	<a href="/about"><span>About</span></a>
	</li>
	<li class="menu-account%s">
	<a href="/account"><span>Account</span></a>
	</li>
	</ul>
	</div>
"""%(home,game,about,account)
	return html

def gen_home():
	html="""	<h1>
	Welcome to PostPrompt
	</h1>
	<p>
	This'll be fun!
	</p>
"""
	return html

def gen_game():
	html="""	<form method="post">
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
	
def gen_account():
	html="""	<p>
	Accounts not implemented yet!
	</p>
"""
	return html
	
def gen_about():
	html="""	<p>
	I'm Quinten!
	</p>
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
