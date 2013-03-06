// comments?
function unDisplayCards(){
	document.getElementById("content").removeChild(document.getElementById("deck_manage"));
}

function displayCards(){
	var game=document.createElement("div");
	game.setAttribute("id","deck_manage");
	document.getElementById("content").appendChild(game);

	var deck=in_deck
	displayCardList(in_deck,'in_deck')
	deck=out_deck
	displayCardList(out_deck,'out_deck')
}

function displayCardList(list,id){
	var i=0;
	var table=document.createElement("table");
	var td=document.createElement("td");
	var tr=document.createElement("td");
	for(i=0;i<list.length;i++){
		td=document.createElement("td");
		tr=document.createElement("td");
		table.appendChild(td)
		div.style.backgroundImage="url(/static/images/cards/"++".png)";
		document.getElementById("game").appendChild(div);
	}
}

function makeDiv(newClass,newId){
	var div = document.createElement("div");
	div.setAttribute("class",newClass);
	div.setAttribute("id",newId);
	div.style.position="absolute";
	div.style.left=newLeft;
	div.style.top=newTop;
	return div;
}
