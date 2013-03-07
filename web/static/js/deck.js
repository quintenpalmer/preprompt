var in_deck = null;
var out_deck = null;

function save_deck(){
	var csrftoken = get_cookie('csrftoken');
	var xmlhttp = new XMLHttpRequest();
	var i;
	xmlhttp.onreadystatechange=function(){
		if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
			redisplay_cards();
		}
	}
	xmlhttp.open("POST",'',true);
	xmlhttp.setRequestHeader("X-CSRFToken",csrftoken);
	xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
	to_send_in_deck = [];
	for(i=0;i<in_deck.length;i++){
		to_send_in_deck.push(in_deck[i][1]);
	}
	var command = "deck="+to_send_in_deck.join()
	xmlhttp.send(command);
}

function display(in_deck_string,out_deck_string){
	var div = document.createElement("div");
	var i=0;
	div.setAttribute("id","deck_manage");
	document.getElementById("content").appendChild(div);

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
	var card_list = create_sub_lists(card_list);
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
				span.onmousedown=function(){add_to_deck(event)};
			}
			else{
				span.onmousedown=function(){remove_from_deck(event)};
			}
			tr.appendChild(td)
		}
		table.appendChild(tr)
	}
	div.appendChild(table)
	document.getElementById("deck_manage").appendChild(div)
}

function create_sub_lists(my_list){
	var col_width = 5;
	var cur_col_width;
	var i = 0;
	var j = 0;
	var ret_list = [];
	var sub_list = null;
	var remaining = my_list.length
	for(i=0;i<my_list.length;i+=col_width){
		sub_list = [];
		cur_col_width = Math.min(col_width,remaining);
		for(j=i;j<i+cur_col_width;j++){
			sub_list.push(my_list[j]);
		}
		remaining -= col_width;
		ret_list.push(sub_list);
	}
	return ret_list;
}

function add_to_deck(event){
	var card_id = event.target.id;
	var card = remove(out_deck,card_id);
	in_deck.push(card);
	redisplay_cards();
}

function remove_from_deck(event){
	var card_id = event.target.id;
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

function get_cookie(name){
    var cookie_value = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].replace(/ /g,'');
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookie_value = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookie_value;
}
