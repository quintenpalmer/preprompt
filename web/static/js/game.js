var game;
var game_id;

function setup_game(){
	console.log('setting up');
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

function play_card_game(event){
	card_id = event.target.id;
	console.log('clicked');
	ajax_request('command=play&params='+card_id,receive_game_xml,url='/play/game/ajax_update_game/'+game_id+'/');
}

function receive_game_xml(xml_string){
	game = make_game(xml_string);
	redisplay_game()
}

function display(xml_string,input_game_id){
	content = document.getElementById("content");
	var game_div = document.createElement("div");
	game_div.setAttribute("id","game");

	content.appendChild(game_div);

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
	display_control_state(game.control_state);
	display_card_lists(them.deck,false,them.hand,true);
	display_card_lists(them.grave,false,them.active,true);
	display_card_lists(me.grave,false,me.active,true);
	display_card_lists(me.deck,false,me.hand,true);
	display_actions();
}

function display_actions(){
	var tds = [["Setup",setup_game],["Draw",draw_game],["Phase",phase_game],["Turn",turn_game]]
	var table = create_table('mini-manage',tds);
	var table_div = document.createElement("div");
	table_div.appendChild(table);

	document.getElementById("game").appendChild(table_div);
}

function display_control_state(control_state){
	var control_state_div = document.createElement("div");
	control_state_div.setAttribute("id","control_state");

	var tds = [[get_super_phase_text(control_state.super_phase),null],[get_phase_text(control_state.phase),null],[control_state.turn_owner,null],[control_state.has_drawn,turn_game]]
	var table = create_table('mini-manage',tds);
	var table_div = document.createElement("div");
	table_div.appendChild(table);

	control_state_div.appendChild(table_div);
	document.getElementById("game").appendChild(control_state_div);
}

function display_card_lists(card_list_left,expand_left,card_list_right,expand_right){
	var card_list_div =document.createElement("div");
	card_list_div.setAttribute("id","card_lists");
	document.getElementById("game").appendChild(card_list_div);
	display_card_list(card_list_left,expand_left,card_list_div);
	display_card_list(card_list_right,expand_right,card_list_div);
}

function display_card_list(card_list,expand,card_list_div){
	//console.log(card_list);
	var li;
	var card_name;
	var ul = document.createElement("ul");
	if(expand){
		var iterations = card_list.cards.length;
	}
	else{
		var iterations = Math.min(1,card_list.cards.length);
	}
	if(iterations > 0){
		for(var index=0;index<iterations;index++){
			card_name = card_list.cards[index].name;
			if(card_name == 'Unknown'){
				card_name = '';
			}
			li = create_li(card_name,play_card_game,index);
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
