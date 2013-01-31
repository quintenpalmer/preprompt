
def draw_game(game):
	out = 'Enemy: ' + game.them.player.name+'\n'
	out += '[deck]\t'
	for card in game.them.collection.hand.cards:
		out += card.name
		for i in range(10-len(card.name)):
			out += ' '
	out += '\n'
	out += '[grave]\t' 
	for card in game.them.collection.active.cards:
		out += card.name
		for i in range(10-len(card.name)):
			out += ' '
	out += '\n'
	out += '\n'
	out += '[grave]\t' 
	for card in game.me.collection.active.cards:
		out += card.name
		for i in range(10-len(card.name)):
			out += ' '
	out += '\n'
	out += '[deck]\t'
	for card in game.me.collection.hand.cards:
		out += card.name
		for i in range(10-len(card.name)):
			out += ' '
	out += '\n'
	out += 'You: ' + game.me.player.name+'\n'
	print out
