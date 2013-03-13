var in_deck = null;
var out_deck = null;

function save_deck(){
	to_send_in_deck = [];
	for(i=0;i<in_deck.length;i++){
		to_send_in_deck.push(in_deck[i][1]);
	}
	var command = "deck="+to_send_in_deck.join()
	ajax_request(command,redisplay_cards,'');
}

function display(in_deck_string,out_deck_string){
	content = document.getElementById("content");
	var div = document.createElement("div");
	div.setAttribute("id","deck_manage");

	var table = document.createElement("table");
	table.setAttribute("id","mini-manage");
	var tr = document.createElement("tr");
	var td = document.createElement("td");
	var a = document.createElement("a");
	var span = document.createElement("span");
	span.onclick=function(){save_deck()};
	span.innerHTML="Load"
	a.appendChild(span);
	td.appendChild(a);
	tr.appendChild(td);
	table.appendChild(tr);

	content.appendChild(table);
	content.appendChild(div);

	var i=0;
	in_deck = in_deck_string.split(',');
	if(in_deck[0]==""){
		in_deck = [];
	}
	for(i=0;i<in_deck.length;i++){
		in_deck[i] = in_deck[i].split('_');
	}
	out_deck = out_deck_string.split(',');
	if(out_deck[0]==""){
		out_deck = [];
	}
	for(i=0;i<out_deck.length;i++){
		out_deck[i] = out_deck[i].split('_');
	}
	display_cards(in_deck,'in_deck');
	display_cards(out_deck,'out_deck');
}

function undisplay_cards(){
	document.getElementById("content").removeChild(document.getElementById("deck_manage"));
	var div = document.createElement("div");
	div.setAttribute("id","deck_manage");
	document.getElementById("content").appendChild(div);
}

function redisplay_cards(){
	undisplay_cards();
	display_cards(in_deck,'in_deck');
	display_cards(out_deck,'out_deck');
}

function display_cards(card_list,div_id){
	var div = document.createElement("div");
	var table = document.createElement("table");
	table.setAttribute("id","mini-manage");
	var card_list = create_sub_lists(card_list,5);
	var index = 0;
	var sub_index = 0;
	var tr = null;
	var td = null;
	var span = null;
	for(index=0;index<card_list.length;index++){
		tr = document.createElement("tr");
		sub_card_list = card_list[index];
		for(sub_index=0;sub_index<sub_card_list.length;sub_index++){
			card = sub_card_list[sub_index];
			card_name = card[0];
			card_id = card[1];
			td = document.createElement("td");
			span = document.createElement("span");
			span.setAttribute("id",card_id);
			span.innerHTML="Card "+card_name;
			td.appendChild(span)
			if(div_id == 'out_deck'){
				span.onclick=function(){add_to_deck(event.target.id)};
			}
			else{
				span.onclick=function(){remove_from_deck(event.target.id)};
			}
			tr.appendChild(td)
		}
		table.appendChild(tr)
	}
	div.appendChild(table)
	document.getElementById("deck_manage").appendChild(div)
}

function add_to_deck(card_id){
	var card = remove(out_deck,card_id);
	in_deck.push(card);
	redisplay_cards();
}

function remove_from_deck(card_id){
	var card = remove(in_deck,card_id);
	out_deck.push(card);
	redisplay_cards();
}

function remove(card_list,card_id){
	var i=0;
	var j=0;
	for(i=0;i<card_list.length;i++){
		if(card_list[i][1]==card_id){
			var card = card_list[i];
			delete card_list[i];
			for(j=i;j<card_list.length;j++){
				card_list[j]=card_list[j+1];
			}
			card_list.length--;
			return card;
		}
	}
}
