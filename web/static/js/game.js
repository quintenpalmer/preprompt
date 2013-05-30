var game;
var game_id;

function game_setup(){
	ajax_request('command=setup',gameRepr,url='/play/game/ajax_update_game/'+game_id+'/');
}

function game_draw(){
	ajax_request('command=draw',gameRepr,url='/play/game/ajax_update_game/'+game_id+'/');
}

function game_phase(){
	ajax_request('command=phase',gameRepr,url='/play/game/ajax_update_game/'+game_id+'/');
}

function game_turn(){
	ajax_request('command=turn',gameRepr,url='/play/game/ajax_update_game/'+game_id+'/');
}

function game_play_card_from_hand(event){
	console.log(event);
	card_id = event.target.id;
	console.log('play from hand');
	console.log(card_id);
	ajax_request('command=play&params='+card_id,gameRepr,url='/play/game/ajax_update_game/'+game_id+'/');
}

function game_play_card_from_active(event){
	card_id = event.target.id;
	console.log('play from active');
	console.log(card_id);
	ajax_request('command=play&params='+card_id,gameRepr,url='/play/game/ajax_update_game/'+game_id+'/');
}

function gameRepr(gameRepr){
	game = make_game(gameRepr);
	redisplay_game();
}

function display(gameRepr,input_game_id){
	content = document.getElementById("content");
	var game_div = document.createElement("div");
	game_div.setAttribute("id","game");

	content.appendChild(game_div);

	game = make_game(gameRepr);
	game_id = input_game_id;
	display_game();
}

function redisplay_game(){
	undisplay_game();
	display_game();
}

/* Displays all the information on the board. */
/* THIS IS WHERE THINGS SHOULD BE DECLARED TO BE FACE-DOWN!! */
function display_game(){
	var me = game.me;
	var them = game.them;
	display_control_state(game);
	display_player_stats(them);
	// reminder: d_c_lists(list, fanned?, visible?, action, ...)
	display_card_lists(them.deck, false, false, null, them.hand, true, false, null);
	display_card_lists(them.grave, false, true, null, them.active, true, true, null);
	display_card_lists(me.grave, false, true, null, me.active, true, true, game_play_card_from_active);
	display_card_lists(me.deck, false, false, game_draw, me.hand, true, true, game_play_card_from_hand);
	display_player_stats(me);
	display_actions();
}

function display_actions(){
	/* Displays action buttons. */
	var table = document.createElement("table");
		table.setAttribute("class", "mini-info");
	var tr = document.createElement("tr");
	var td_setup = document.createElement("td");
		td_setup.setAttribute("class", "action-setup");
		td_setup.innerHTML = "Setup";
		td_setup.onclick = function() { game_setup() };
	var td_draw = document.createElement("td");
		td_draw.setAttribute("class", "action-draw");
		td_draw.innerHTML = "Draw";
		td_draw.onclick = function() { game_draw() };
	var td_phase = document.createElement("td");
		td_phase.setAttribute("class", "action-phase");
		td_phase.innerHTML = "Phase";
		td_phase.onclick = function() { game_phase() };
	var td_turn = document.createElement("td");
		td_turn.setAttribute("class", "action-turn");
		td_turn.innerHTML = "Turn";
		td_turn.onclick = function() { game_turn() };
	tr.appendChild(td_turn);
	tr.appendChild(td_phase);
	tr.appendChild(td_draw);
	tr.appendChild(td_setup); // n.b. this will be displayed at left
	table.appendChild(tr);
	document.getElementById("game").appendChild(table);
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

function display_player_stats(player) {
	/* Displays player name and health. */
	var table = document.createElement("table");
		table.setAttribute("class", "mini-info");
	var tr = document.createElement("tr");
	var td_name = document.createElement("td");
		td_name.setAttribute("class", "player-name");
		td_name.innerHTML = player.name;
	var td_health = document.createElement("td");
		td_health.setAttribute("class", "player-health");
		td_health.innerHTML = player.health;
	tr.appendChild(td_health);
	tr.appendChild(td_name); // n.b. this will be displayed at left
	table.appendChild(tr);
	document.getElementById("game").appendChild(table);
}

/* Displays a pair of deck/hand or active cards/graveyard:
	left_card_list: The list to be displayed at left in this row
	left_expand: Should the left list be fanned out (T) or piled (F)?
	left_action: The action to be taken on clicking an item.
	left_visible: Should the cards be face-up (T) or face-down (F)?
	right_parameters are the same for the right side. */
function display_card_lists(left_card_list, left_expand, left_visible, left_action, right_card_list, right_expand, right_visible, right_action) {
	var card_list_div = document.createElement("div");
	card_list_div.setAttribute("class", "card_lists");
	document.getElementById("game").appendChild(card_list_div);
	display_card_list(left_card_list, left_expand, card_list_div, left_visible, left_action);
	display_card_list(right_card_list, right_expand, card_list_div, right_visible, right_action);
}

/* Displays a single list of cards on the board:
	card_list: The list to be displayed.
	expand: Should the list be fanned (T) or piled (F)?
	card_list_div: The div to be the container for this list.
	visible: Should the list be face-up (T) or face-down (F)?
	action: The action to be taken on clicking an item. */
function display_card_list(card_list, expand, card_list_div, visible, action){
	//console.log(card_list);
	var li;
	var card_name;
	var ul = document.createElement("ul");
		ul.setAttribute("class", "list_box");
	if (expand) {
		var iterations = card_list.cards.length; // as many iterations as cards
	}
	else { // display one if the list has at least one; otherwise, none
		var iterations = Math.min(1, card_list.cards.length);
	}
	if (iterations > 0) {
		for (var index=0; index < iterations; index++ ){ // for each card in list
			card_name = card_list.cards[index].name; // get its name
			if (card_name == 'Unknown'){
				card_name = '';
			}
			if (visible) {
				card = display_icon(index, action, card_name);
				li = document.createElement("li").appendChild(card);
			} else {
				li = document.createElement("li").appendChild(display_back());
			//	li.innerHTML = "&nbsp;";
				li.setAttribute("id", index);
			}
			ul.appendChild(li); // add this card to the list
		}
	}
	card_list_div.appendChild(ul);
}

function undisplay_game(){
	document.getElementById("content").removeChild(document.getElementById("game"));
	var div = document.createElement("div");
	div.setAttribute("id","game");
	document.getElementById("content").appendChild(div);
}
