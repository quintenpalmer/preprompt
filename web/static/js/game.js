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
	console.log('clicked');
	ajax_request('command=play&params='+card_id,receive_game_xml,url='/play/game/ajax_update_game/'+game_id+'/');
}

function receive_game_xml(xml_string){
	game = make_game(xml_string);
	redisplay_game()
}

function display(xml_string,input_game_id){
	content = document.getElementById("content");
	var div = document.createElement("div");
	div.setAttribute("id","game");

	var tr;
	var td;
	var a;
	var span;
	var table = document.createElement("table");
	table.setAttribute("id","mini-manage");
	tr = document.createElement("tr");

	td = document.createElement("td");
	a = document.createElement("a");
	span = document.createElement("span");
	span.onclick=function(){setup_game()};
	span.innerHTML="Setup"
	a.appendChild(span);
	td.appendChild(a);
	tr.appendChild(td);

	td = document.createElement("td");
	a = document.createElement("a");
	span = document.createElement("span");
	span.onclick=function(){draw_game()};
	span.innerHTML="Draw"
	a.appendChild(span);
	td.appendChild(a);
	tr.appendChild(td);

	td = document.createElement("td");
	a = document.createElement("a");
	span = document.createElement("span");
	span.onclick=function(){phase_game()};
	span.innerHTML="Phase"
	a.appendChild(span);
	td.appendChild(a);
	tr.appendChild(td);

	td = document.createElement("td");
	a = document.createElement("a");
	span = document.createElement("span");
	span.onclick=function(){turn_game()};
	span.innerHTML="Turn"
	a.appendChild(span);
	td.appendChild(a);
	tr.appendChild(td);

	table.appendChild(tr);

	content.appendChild(table);
	content.appendChild(div);

	game = make_game(xml_string);
	game_id = input_game_id;
	display_game();
}

function redisplay_game(){
	undisplay_game();
	display_game();
}

function display_game(){
	var me = game.me.collection;
	var them = game.them.collection;
	display_card_lists(me.deck,false,me.hand,true);
	display_card_lists(me.grave,false,me.active,true);
	display_card_lists(them.grave,false,them.active,true);
	display_card_lists(them.deck,false,them.hand,true);
}

function display_card_lists(card_list_left,expand_left,card_list_right,expand_right){
	var card_list_div =document.createElement("div");
	card_list_div.setAttribute("id","card_lists");
	document.getElementById("game").appendChild(card_list_div)
	display_card_list(card_list_left,expand_left,card_list_div);
	display_card_list(card_list_right,expand_right,card_list_div);
}

function display_card_list(card_list,expand,card_list_div){
	//console.log(card_list);
	var li;
	var a;
	var span;
	var ul = document.createElement("ul");
	if(expand){
		var iterations = card_list.cards.length;
	}
	else{
		var iterations = Math.min(1,card_list.cards.length);
	}
	if(iterations > 0){
		for(var index=0;index<iterations;index++){
			li = document.createElement("li");
			li.onclick=function(){play_card_game(event.target.id)};
			span = document.createElement("span");
			span.innerHTML=card_list.cards[index].name;
			span.setAttribute('id',index);
			li.appendChild(span);
			ul.appendChild(li);
		}
	}
	else{
		li = document.createElement("li");
		ul.appendChild(li);
	}
	card_list_div.appendChild(ul);
}

function undisplay_game(){
	document.getElementById("content").removeChild(document.getElementById("game"));
	var div = document.createElement("div");
	div.setAttribute("id","game");
	document.getElementById("content").appendChild(div);
}
