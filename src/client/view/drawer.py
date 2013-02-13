from pyplib.errors import PP_Model_Error
import sys

def init_screen():
	#sys.stdout.write('\n'*11)
	pass
def draw(model,message):
	#sys.stdout.write('\33[10A]                                        \r')
	sys.stdout.write(message+'\n')
	try:
		sys.stdout.write(draw_game(model.get_current_game()))
	except PP_Model_Error as e:
		sys.stdout.write("No current game! "+str(e)+'\n'*1)#0)

def draw_game(game):
	out = '='*70+'\n'
	out += 'State: ' + str(game.control_state.super_phase) + '/' + str(game.control_state.phase) + ' ' + str(game.control_state.turn_owner)+'\n'
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
	out += '\n'

	return out
