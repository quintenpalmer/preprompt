function make_game(resp){
	console.log(resp);
	var obj = parseJson(resp);
	var respType = obj.respType
	console.log(respType);
	if(respType == 'ok'){
		var command = obj.command
		var gameRepr = obj.gameRepr
		var game = new Game(gameRepr);
		return game;
	}
	else{
		var error_message = obj.error_message;
		return 'Received error message: '+respType+' : '+error_message;
	}
}

function Game(obj){
	console.log("---------");
	console.log(obj);
	obj = obj.game
	this.me = new Player(obj.me);
	this.them = new Player(obj.them);
	this.super_phase = obj.superPhase;
	this.phase = obj.phase;
	this.turn_owner = obj.turnOwner;
	this.has_drawn = obj.hasDrawn;
}

function Player(obj){
	this.uid = obj.uid;
	this.name = obj.name;
	this.health = obj.health;
	this.deck    = new Card_List(obj.deck);
	this.hand    = new Card_List(obj.hand);
	this.active  = new Card_List(obj.active);
	this.grave   = new Card_List(obj.grave);
	this.special = new Card_List(obj.special);
}

function Card_List(obj){
	this.cards = [];
	var card_names = obj.cards
	for(var i=0;i<card_names.length;i++){
		this.cards.push(new Card(card_names[i]));
	}
}

function Card(obj){
	this.name = obj.name
}

var super_phase_setup = '0';
var super_phase_main = '1';
var super_phase_end = '2';

function get_super_phase_text(super_phase){
	if(super_phase == super_phase_setup){
		return "Setup";
	}
	else if(super_phase == super_phase_main){
		return "Main Gameplay";
	}
	else if(super_phase == super_phase_end){
		return "Game End";
	}
	else{
		return "Unknown Super Phase";
	}
}

var phase_draw = '0';
var phase_pre = '1';
var phase_main = '2';
var phase_end = '3';

function get_phase_text(phase){
	if(phase == phase_draw){
		return "Draw Phase";
	}
	else if(phase == phase_pre){
		return "Pre Phase";
	}
	else if(phase == phase_main){
		return "Main Phase";
	}
	else if(phase == phase_end){
		return "End Phase";
	}
	else{
		return "Unknown Phase";
	}
}
