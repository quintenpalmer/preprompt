from pplib import database

def register_add_cards(username):
	db = database.Database()
	uid = int(db.select("select id from auth_user where username='%s'"%username)[0][0])
	starting_cards = [x[0] for x in db.select('select card_name_id from play_starting_cards')]
	values_list = []
	start_index = len(db.select('select id from play_cards'))+1
	for i, card in enumerate(starting_cards):
		db.update('insert into play_cards values(%s,%s,%s)'%(i+start_index,card,uid))
	cards = [x[0] for x in db.select("select id from play_cards where uid='%s'"%uid)]
	values_list = []
	start_index = len(db.select('select id from play_decks'))+1
	for i,card in enumerate(cards):
		db.update('insert into play_decks values(%s,%s,0,%s)'%(i+start_index,card,uid))
