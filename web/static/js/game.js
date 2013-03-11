var game;
var game_id;

function setup_game(){
	ajax_request('command=setup',receive_game_xml,url='/play/game/ajax_update_game/'+game_id+'/');
}

function draw_game(){
	ajax_request('command=draw',receive_game_xml,url='/play/game/ajax_update_game/'+game_id+'/');
}

function phase_game(){
	ajax_request('command=phase',receive_game_xml,url='/play/game/ajax_update_game/'+game_id+'/');
}

function turn_game(){
	ajax_request('command=turn',receive_game_xml,url='/play/game/ajax_update_game/'+game_id+'/');
}

function play_card_game(card_id){
	ajax_request('command=play&param='+card_id,receive_game_xml,url='/play/game/ajax_update_game/'+game_id+'/');
}

function receive_game_xml(xml_string){
	game = make_game(xml_string);
	redisplay_game()
}

function display(xml_string,input_game_id){
	var div = document.createElement("div");
	div.setAttribute("id","game");
	document.getElementById("content").appendChild(div);
	game = make_game(xml_string);
	game_id = input_game_id;
	display_game();
}

function redisplay_game(){
	undisplay_game();
	display_game();
}

function display_game(){
	//console.log(game);
	
	display_card_list(game.me.collection.deck,false)
	//display_card_list(game.me.collection.grave,false)
	display_card_list(game.me.collection.hand,true)
	display_card_list(game.me.collection.active,true)
	display_card_list(game.them.collection.active,true)
	display_card_list(game.them.collection.hand,true)
	//display_card_list(game.them.collection.grave,false)
	display_card_list(game.them.collection.deck,false)
}

function display_card_list(card_list,expand){
	console.log(card_list);
	var card_list_div =document.createElement("div");
	card_list_div.setAttribute("id","card_lists");
	var td;
	var tr;
	var a;
	var span;
	var table = document.createElement("table");
	tr = document.createElement("tr");
	if(expand){
		var iterations = card_list.cards.length;
	}
	else{
		var iterations = 1;
	}
	for(var index=0;index<iterations;index++){
		td = document.createElement("td");
		span = document.createElement("span");
		span.innerHTML="Game "+card_list.cards[index].name;
		span.setAttribute('id',card_list.cards[index].name);
		span.onmousedown=function(){play_card_game(event.target.id)};
		td.appendChild(span);
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
