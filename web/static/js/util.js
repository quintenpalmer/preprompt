/* Get cookie of given name */
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

/* Returns a list of lists from the given input list
   where each sublist is of lengh col_width */
function create_sub_lists(my_list,col_width){
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

/* Sends an ajax request of 'command'
   with the callback function 'callback'
   and the url 'url' */
function ajax_request(command,callback,url){
	var csrftoken = get_cookie('csrftoken');
	var xmlhttp = new XMLHttpRequest();
	var i;
	xmlhttp.onreadystatechange=function(){
		if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
			callback(xmlhttp.responseText);
		}
	}
	xmlhttp.open("POST",url,true);
	xmlhttp.setRequestHeader("X-CSRFToken",csrftoken);
	xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
	xmlhttp.send(command);
}

/* XML parsing functions */
function parse_xml(xml_string){
	var parser=new DOMParser();
	return parser.parseFromString(xml_string,"text/xml");
}
function parse_element(element,tag){
	return element.getElementsByTagName(tag)[0];
}

function parse_elements(element,tag){
	return element.getElementsByTagName(tag);
}
function parse_ints(element,tag){
	var elements = parse_elements(element,tag);
	var ints = [];
	for(var i=0;i<elements.length;i++){
		ints.push(parseInt(elements[i].firstChild.nodeValue));
	}
	return ints;
}
function parse_string(element,tag){
	return parse_element(element,tag).firstChild.nodeValue
}
function parse_bool(element,tag){
	return parse_string(element,tag) == 'True';
}
function parse_int(element,tag){
	return parseInt(parse_string(element,tag));
}

/* Create custom element groups */

/* Create li item with
   innerHTML 'li_html',
   onclick function 'li_onclick', and
   id 'id'
 */
function create_card_li(li_html,li_onclick,li_id){
	var li;
	var a;
	var span;
	li = document.createElement("li");
	span = document.createElement("span");
	if(li_onclick != null){
		span.onclick=function(){li_onclick(event)};
	}
	if(li_id != null){
		span.setAttribute('id',li_id);
	}
	span.innerHTML = li_html;
	li.appendChild(span);
	return li
}

function create_table_data(td_html,td_onclick){
	var td = document.createElement("td");
	var a = document.createElement("a");
	var span = document.createElement("span");
	span.onclick=function(){td_onclick()};
	span.innerHTML=td_html;
	a.appendChild(span);
	td.appendChild(a);
	return td;
}

function create_table(id,tds,max_width){
	var table = document.createElement("table");
	var tr;
	var td;
	var tds_sub;
	var td_sub;
	var name;
	var action;
	var sub_index;
	var tds = create_sub_lists(tds,max_width);
	table.setAttribute("id",id);
	for(var index=0;index<tds.length;index++){
		tr = document.createElement("tr");
		tds_sub = tds[index];
		for(sub_index=0;sub_index<tds_sub.length;sub_index++){
			td_sub = tds_sub[sub_index];
			name = td_sub[0];
			action = td_sub[1];
			td = create_table_data(name,action);
			tr.appendChild(td);
		}
		table.appendChild(tr);
	}
	return table;
}
