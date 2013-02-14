from model.game import Game
from model.player import Player_Container, Player
from model.collection import Collection
from control.loaded_effects import lookup_table
from pyplib.errors import PP_Load_Error
import os

card_id_to_card_text = {}

def load_card_key_text():
	if card_id_to_card_text == {}:
		try:
			path = os.path.join(os.environ['pyproot'],'opt','postprompt','tables','cards','relation.table')
			f = open(path,'r')
			for line in f.readlines():
				key,val = line.split(':')
				if not card_id_to_card_text.has_key(int(key)):
					card_id_to_card_text[int(key)] = val.strip()
				else:
					raise PP_Load_Error("Duplicate keys in relation table: %s"%key)
			if card_id_to_card_text == {}:
				raise PP_Load_Error("No data in the relation table")
		except IOError:
			raise PP_Load_Error("Could not load the relation table")

def get_game(config_args):
	load_card_key_text()
	player1 = config_args.config_player1
	player2 = config_args.config_player2
	uids = [player1.uid,player2.uid]
	dids = [player1.did,player2.did]
	card_names = ['farts','fresh','persist']
	players = []
	for i in range(0,2):
		player = Player(uid=uids[i])
		cards = []
		try:
			path = os.path.join(os.environ['pyproot'],'opt','postprompt','tables','decks',str(uids[i])+'.table')
			f = open(path,'r')
			decks = {}
			for line in f.readlines():
				key,val = line.split(':')
				decks[int(key)] = val.strip().split(',')
			deck = decks[dids[i]]
			f.close()
		except IOError or IndexError or KeyError:
			raise PP_Load_Error("Could not load the player's deck")
		for card_id in deck:
			cards.append(lookup_table(get_card_key_text_from_id(card_id)))
		verify_deck(cards)
		player_collection = Collection(cards=cards)
		players.append(Player_Container(player=player,collection=player_collection))

	return Game(player1=players[0],player2=players[1])

def verify_deck(cards):
	if len(cards) < 40:
		raise PP_Load_Error("Not enough cards in the player's deck, only %s, needs 40"%str(len(cards)))

def get_card_key_text_from_id(card_id):
	try:
		text = card_id_to_card_text[int(card_id)]
		return text
	except ValueError:
		raise PP_Load_Error("Player deck data contained card id %s which is not an int"%str(card_id))
	except KeyError:
		raise PP_Load_Error("Player deck data contained card id %s is not a valid card id"%str(card_id))
