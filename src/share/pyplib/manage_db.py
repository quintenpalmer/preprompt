from pyplib import database

def register_add_cards(username):
	uid = int(database.select('auth_user','id',where=(("username='"+username+"'"),))[0])
	starting_cards = database.select('play_starting_cards','card_name_id')
	values_list = []
	for card in starting_cards:
		values_list.append((None,card,uid))
	database.insert_batch('play_cards',(int,int,int),values_list)
	cards = database.select('play_cards','id',where=(('uid='+str(uid)),))
	values_list = []
	for card in cards:
		values_list.append((None,uid,0,card))
	database.insert_batch('play_decks',(int,int,int,int),values_list)
