def draw(model):
	if model.current_game_id != None:
		draw_game(model.get_current_game())
	else:
		print "No current game!"

def draw_game(game):
	out = '='*70+'\n'
	out += 'Enemy: ' + game.them.player.name+' Health: '+str(game.them.player.health)+'\n'
	out += '[[DECK]]\t'
	for card in game.them.collection.hand.cards:
		out += '['+card.name+']'
		for i in range(10-len(card.name)):
			out += ' '
	out += '\n'
	if len(game.them.collection.grave.cards) == 0:
		out += '[[GRAVE]]\t'
	else:
		out += '[['+game.them.collection.grave.cards[0].name+']]\t' 
	for card in game.them.collection.active.cards:
		out += '['+card.name+']'
		for i in range(10-len(card.name)):
			out += ' '
	out += '\n'
	if len(game.me.collection.grave.cards) == 0:
		out += '[[GRAVE]]\t'
	else:
		out += '[['+game.me.collection.grave.cards[0].name+']]\t' 
	for card in game.me.collection.active.cards:
		out += '['+card.name+']'
		for i in range(10-len(card.name)):
			out += ' '
	out += '\n'
	out += '[[DECK]]\t'
	for card in game.me.collection.hand.cards:
		out += '['+card.name+']'
		for i in range(10-len(card.name)):
			out += ' '
	out += '\n'
	out += 'You: ' + game.me.player.name+' Health: '+str(game.me.player.health)+'\n'
	out += '-'*70

	print out
