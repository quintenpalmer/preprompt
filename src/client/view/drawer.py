import sys

from pplib.errors import PP_Model_Error

def init_screen():
	#sys.stdout.write('\n'*11)
	pass
def draw(model,message):
	#sys.stdout.write('\33[10A]                                        \r')
	ret = '%s\n'%message
	try:
		ret += draw_game(model.get_current_game())
	except PP_Model_Error as e:
		ret += "No current game! %s\n"%str(e)
	return ret

def draw_game(game):
	out = '='*70+'\n'
	out += 'State: ' + str(game.super_phase) + '/' + str(game.phase) + ' ' + str(game.turn_owner)+'\n'
	out += 'Enemy: ' + game.them.name+' Health: '+str(game.them.health)+'\n'
	out += str(len(game.them.deck.cards))
	out += '\n'
	out += '[[DECK ]]\t'
	for card in game.them.hand.cards:
		out += '['+card.name+']'
		for i in range(10-len(card.name)):
			out += ' '
	out += '\n'
	if len(game.them.grave.cards) == 0:
		out += '[[GRAVE]]\t'
	else:
		out += '[['+game.them.grave.cards[0].name+']]\t'
	for card in game.them.active.cards:
		out += '['+card.name+']'
		for i in range(10-len(card.name)):
			out += ' '
	out += '\n'
	if len(game.me.grave.cards) == 0:
		out += '[[GRAVE]]\t'
	else:
		out += '[['+game.me.grave.cards[0].name+']]\t'
	for card in game.me.active.cards:
		out += '['+card.name+']'
		for i in range(10-len(card.name)):
			out += ' '
	out += '\n'
	out += '[[DECK ]]\t'
	for card in game.me.hand.cards:
		out += '['+card.name+']'
		for i in range(10-len(card.name)):
			out += ' '
	out += '\n'
	out += str(len(game.me.deck.cards))
	out += '\n'
	out += 'You: ' + game.me.name+' Health: '+str(game.me.health)+'\n'
	out += '-'*70
	out += '\n'

	return out
