var games;

function new_game(){
	var command = 'command=new'
	ajax_request(command,receiveGameIds,url='/play/games/ajax_new_game/');
}

function receiveGameIds(game_ids){
	console.log(game_ids);
	games = game_ids.split(',');
	if(games[0]==""){
		games = [];
	}
	redisplay_games()
}

function display(game_ids){
	var div = document.createElement("div");
	var i=0;
	div.setAttribute("id","games");
	document.getElementById("content").appendChild(div);
	games = game_ids.split(',');
	if(games[0]==""){
		games = [];
	}
	display_all_games();
}

function redisplay_games(){
	undisplay_games();
	display_all_games();
}

function display_all_games(){
	console.log(games);
	var td;
	var tr;
	var a;
	var span;
	var index;
	var table = document.createElement("table");
	table.setAttribute("id","manage");
	for(index=0;index<games.length;index++){
		td = document.createElement("td");
		tr = document.createElement("tr");
		a = document.createElement("a");
		span = document.createElement("span");
		span.setAttribute('class','bigbutton');
		span.innerHTML="Game "+games[index];
		a.setAttribute('href','/play/game/'+games[index]);
		a.appendChild(span);
		td.appendChild(a);
		tr.appendChild(td);
		table.appendChild(tr);
	}
	document.getElementById("games").appendChild(table)
}

function undisplay_games(){
	document.getElementById("content").removeChild(document.getElementById("games"));
	var div = document.createElement("div");
	div.setAttribute("id","games");
	document.getElementById("content").appendChild(div);
}
