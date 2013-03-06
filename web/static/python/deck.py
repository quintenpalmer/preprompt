
def unDisplayCards():
	doc["content"].removeChild(doc["deck_manage"])

def displayCards(in_deck_string,out_deck_string):
	div = DIV()
	div.id = "deck_manage"
	doc["content"].appendChild(div)

	in_deck = in_deck_string.split(',')
	out_deck = out_deck_string.split(',')
	displayCardList(in_deck,'in_deck')
	displayCardList(out_deck,'out_deck')

def displayCardList(card_list,div_id):
	table = TABLE()
	table.id = "mini-manage"
	card_list = create_sub_lists(card_list)
	for card_sub in card_list:
		tr = TR()
		for card in card_sub:
			td = TD()
			td <= SPAN('Card '+card)
			tr <= td
		table <= tr
	doc["content"] <= table

def create_sub_lists(my_list):
	col_width = 5
	return [my_list[i:i+col_width] for i in range(0,len(my_list), col_width)]
