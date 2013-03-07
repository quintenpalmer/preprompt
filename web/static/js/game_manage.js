
function new_game(){
	var command = 'command=new'
	ajax_request(command,display_new_games);
}

function display_new_games(){
	var table = document.getElementById("manage");
	console.log(table)
	var td = document.createElement("td");
	var tr = document.createElement("tr");
	var a = document.createElement("a");
	var span = document.createElement("span");
	span.innerHTML="Game "
	a.setAttribute('href','/game/play/')
	a.appendChild(span)
	td.appendChild(a)
	tr.appendChild(td)
	table.appendChild(tr)
}
