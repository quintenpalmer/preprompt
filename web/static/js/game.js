var game;
var game_id;

function game_setup(){
	ajax_request('command=setup',receive_game_xml,url='/play/game/ajax_update_game/'+game_id+'/');
}

function game_draw(){
	ajax_request('command=draw',receive_game_xml,url='/play/game/ajax_update_game/'+game_id+'/');
}

function game_phase(){
	ajax_request('command=phase',receive_game_xml,url='/play/game/ajax_update_game/'+game_id+'/');
}

function game_turn(){
	ajax_request('command=turn',receive_game_xml,url='/play/game/ajax_update_game/'+game_id+'/');
}

function game_play_card_from_hand(event){
	card_id = event.target.id;
	console.log('clicked');
	ajax_request('command=play&params='+card_id,receive_game_xml,url='/play/game/ajax_update_game/'+game_id+'/');
}

function game_play_card_from_active(event){
	card_id = event.target.id;
	console.log('clicked');
	ajax_request('command=play&params='+card_id,receive_game_xml,url='/play/game/ajax_update_game/'+game_id+'/');
}

function receive_game_xml(xml_string){
	game = make_game(xml_string);
	redisplay_game();
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
	display_player_stats(game.them.player);
	display_card_lists(them.deck,false,null,them.hand,true,null);
	display_card_lists(them.grave,false,null,them.active,true,null);
	display_card_lists(me.grave,false,null,me.active,true,game_play_card_from_active);
	display_card_lists(me.deck,false,game_draw,me.hand,true,game_play_card_from_hand);
	display_player_stats(game.me.player);
	display_actions();
}

function display_actions(){
	var tds = [["Setup",game_setup],["Draw",game_draw],["Phase",game_phase],["Turn",game_turn]]
	var table = create_table('mini-manage',tds,4);
	var table_div = document.createElement("div");
	table_div.appendChild(table);

	document.getElementById("game").appendChild(table_div);
}

function display_control_state(control_state){
	var control_state_div = document.createElement("div");

	if(control_state.super_phase==super_phase_setup || control_state.super_phase==super_phase_end){
		var tds = [[get_super_phase_text(control_state.super_phase)+" Phase",null]];
		var table = create_table('mini-info',tds,1);
	}
	else{
		var tds = [[get_phase_text(control_state.phase),null],[control_state.turn_owner,null],[control_state.has_drawn,game_turn]]
		var table = create_table('mini-info',tds,3);
	}
	var table_div = document.createElement("div");
	table_div.appendChild(table);

	control_state_div.appendChild(table_div);
	document.getElementById("game").appendChild(control_state_div);
}

function display_player_stats(player){
	var table_div = document.createElement("div");
	var tds = [[player.name,null],[player.health,null]];
	var table = create_table('mini-info',tds,2);
	var table_div = document.createElement("div");
	table_div.appendChild(table);
	document.getElementById("game").appendChild(table_div);
}

function display_card_lists(left_card_list,left_expand,left_action,right_card_list,right_expand,right_action){
	var card_list_div =document.createElement("div");
	card_list_div.setAttribute("id","card_lists");
	document.getElementById("game").appendChild(card_list_div);
	display_card_list(left_card_list,left_expand,card_list_div,left_action);
	display_card_list(right_card_list,right_expand,card_list_div,right_action);
}

function display_card_list(card_list,expand,card_list_div,action){
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
			li = create_card_li(card_name,action,index);
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
