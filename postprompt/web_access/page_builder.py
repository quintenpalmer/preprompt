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
	url = url[0]
	home=game=about=account=''
	if url=='':
		home='-current'
	elif url=='game':
		game='-current'
	elif url=='about':
		about='-current'
	elif url=='account':
		account='-current'
	html="""
	<div id="menubar">
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

def gen_req_login():
	html="""<p>
	Need to be logged in to do that!
	<a href="/account/login">Login</a> <a href="/account/register">Register</a>
	</p>
"""
	return html
	
def gen_about():
	html="""<p>
	I'm Quinten!
	</p>
"""
	return html

def gen_dummy():
	html="""<p>
		This is a dummy page!
	</p>
"""
	return html

def gen_not_found():
	html="""<p>
		404 - Page not found
	</p>
"""
	return html

def gen_register():
	html="""<div id="register">
	<h1>
		Register
	</h1>
	<form action="/account/register/" method="post">
		<table>
		<tr>
			<td>Username: </td>
			<td><input class="inputbox" type="text" name="runame"></input><br></td>
		</tr>
		<tr>
			<td>Password: </td>
			<td><input class="inputbox" type="password" name="rpass"></input><br></td>
		</tr>
		<tr>
			<td>Retype Password: </td>
			<td><input class="inputbox" type="password" name="rpass2"></input><br></td>
		</tr>
		<tr>
			<td>Nickname: </td>
			<td><input class="inputbox" type="text" name="rnickname"></input><br></td>
		</tr>
		<tr>
			<td><input type="submit" value="Register"/></td>
		<tr>
		</table>
	</form>
</div>
"""
	return html

def gen_login():
	html="""<div id="login">
	<h1>
		Login
	</h1>
	<form action="/account/login" method="post">
		<table>
		<tr>
			<td>Username: </td>
			<td><input class="inputbox" type="text" name="luname"></input><br></td>
		</tr>
		<tr>
			<td>Password: </td>
			<td><input class="inputbox" type="password" name="lpass"></input><br></td>
		</tr>
		<tr>
			<td><input type="submit" value="Login"/></td>
		</tr>
		</table>
	</form>
</div>
"""
	return html

def gen_welcome():
	html="""<p>
		Welcome, %s!
	</p>
"""
	return html

def gen_improper_login():
	html="""<p>
		Improper username/password for %s!
	</p>
"""
	return html

def gen_internal_error():
	html="""<p>
		500 - Internal Error
	</p>
"""
	return html

def gen_password_mismatch():
	html="""<p>
		Passwords did not match!
	</p>
"""
	return html

def gen_username_exists():
	html="""<p>
		Username %s already exists!
	</p>
"""
	return html

def gen_success_account():
	html="""<p>
		Congrats %s on making your account!
	</p>
"""
	return html

def gen_game_splash():
	html="""<p>
	<table id="manage">
		<tr>
			<td>
				<a href="/game/play"><span>Start Playing</span></a>
			</td>
			<td>
				<a href="/game/manage"><span>Manage Decks</span></a>
			</td>
		</tr>
	</table>
	</p>
"""
	return html

def gen_account():
	html="""<p>
	Welcome to the account management page %s!
	</p>
"""
	return html
