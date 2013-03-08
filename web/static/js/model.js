function Card_List(element){
	this.cards = [];
	var card_names = parse_elements(element,'card');
	for(var i=0;i<card_names.length;i++){
		this.cards.push(new Card(card_names[i]));
	}
}

function Card(element){
	var card_type = parse_string(element,'type')
	if(card_type == 'full'){
		this.name = parse_string(element,'name')
	}
	else{
		this.name = card_type
	}
}

function Collection(element){
	this.deck    = new Card_List(parse_element(element,'deck'));
	this.hand    = new Card_List(parse_element(element,'hand'));
	this.active  = new Card_List(parse_element(element,'active'));
	this.grave   = new Card_List(parse_element(element,'grave'));
	this.special = new Card_List(parse_element(element,'special'));
}

function Control_State(element){
	this.super_phase = parse_int(element,'super_phase');
	this.phase = parse_int(element,'phase');
	this.turn_owner = parse_int(element,'turn_owner');
	this.has_drawn = parse_bool(element,'has_drawn');
}

function Game(element){
	this.me = new Player_Container(parse_element(element,'me'));
	this.them = new Player_Container(parse_element(element,'them'));
	this.control_state = new Control_State(parse_element(element,'control_state'));
}

function Player_Container(element){
	this.player = new Player(parse_element(element,'player'));
	this.collection = new Collection(parse_element(element,'collection'));
}

function Player(element){
	this.uid = parse_int(element,'uid');
	this.name = parse_string(element,'name');
	this.health = parse_int(element,'health');
}

function make_game(resp){
	var ele = parse_xml(resp);
	var resp_status = parse_string(ele,'resp_status');
	if(resp_status == 'ok'){
		var game_state = parse_element(ele,'game_xml');
		var game = new Game(game_state);
		console.log(game);
		console.log(this);
		return game;
	}
	else{
		var error_message = parse_string(ele,'error_message');
		if(resp_status == 'bad_xml_request'){
			util.logger.warning('Last Request had bad xml data: '+error_message);
		}
		else if(resp_status == 'invalid_game_action'){
			util.logger.warning('Last Request had an invalid game action: '+error_message);
		}
		else if(resp_status == 'invalid_model_action'){
			util.logger.warning('Last Request had an invalid model action: '+error_message);
		}
		return 'Received error message: '+error_message;
	}
}
