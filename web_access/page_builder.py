def build_full_page():
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
	return html
