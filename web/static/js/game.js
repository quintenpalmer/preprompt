var game;

function update_game(game_id){
	var command = 'command=setup'
	ajax_request(command,receive_game_xml,url='/play/game/ajax_update_game/'+game_id+'/');
}

function receive_game_xml(xml_string){
	game = make_game(xml_string);
	redisplay_game()
}

function display(xml_string){
	var div = document.createElement("div");
	div.setAttribute("id","game");
	document.getElementById("content").appendChild(div);
	game = make_game(xml_string);
	display_game();
}

function redisplay_game(){
	undisplay_game();
	display_game();
}

function display_game(){
	//console.log(game);
	display_card_list(game.me.collection.deck)
}

function display_card_list(card_list){
	console.log(card_list);
	var card_list_div =document.createElement("div");
	card_list_div.setAttribute("id","card_lists");
	var td;
	var tr;
	var a;
	var span;
	var table = document.createElement("table");
	tr = document.createElement("tr");
	for(var index=0;index<card_list.cards.length;index++){
		td = document.createElement("td");
		a = document.createElement("a");
		span = document.createElement("span");
		span.innerHTML="Game "+card_list.cards[index].name;
		a.setAttribute('href','/play/game/'+card_list.cards[index].name);
		a.appendChild(span);
		td.appendChild(a);
		tr.appendChild(td);
	}
	table.appendChild(tr);
	card_list_div.appendChild(table);
	document.getElementById("game").appendChild(card_list_div)
}

function undisplay_game(){
	document.getElementById("content").removeChild(document.getElementById("game"));
	var div = document.createElement("div");
	div.setAttribute("id","game");
	document.getElementById("content").appendChild(div);
}
