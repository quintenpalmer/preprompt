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
