from model.game import Game
from model.player import Player_Container, Player
from model.collection import Collection
from control.loaded_effects import lookup_table
from pyplib.errors import PP_Load_Error, PP_Database_Error
from pyplib import database
import os

card_id_to_card_text = {}

def load_card_key_text():
	if card_id_to_card_text == {}:
		try:
			cards = database.select('game_cards','*')
			for card in cards:
				key = int(card[0])
				val = card[2]
				if not card_id_to_card_text.has_key(int(key)):
					card_id_to_card_text[int(key)] = val.strip()
				else:
					raise PP_Load_Error("Duplicate keys in relation table: %s"%key)
			if card_id_to_card_text == {}:
				raise PP_Load_Error("No data in the relation table")
		except PP_Database_Error:
			raise PP_Load_Error("Could not load the relation table")

def get_game(config_args):
	load_card_key_text()
	player1 = config_args.config_player1
	player2 = config_args.config_player2
	uids = [player1.uid,player2.uid]
	dids = [player1.did,player2.did]
	players = []
	for i in range(0,2):
		player = Player(uid=uids[i])
		cards = []
		try:
			deck = [int(card_id) for card_id in database.select('game_decks','card_ids',where=('uid='+str(uids[i]),'deck_id='+str(dids[i])))[0][0].split(',')]
		except Exception:
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
