
def serialize(data):
	out_str = '<resp>'
	out_str += '<resp_status>'
	out_str += str(data.pop(0))
	out_str += '</resp_status>'
	out_str += '<resp_type>'
	out_str += str(data.pop(0))
	out_str += '</resp_type>'
	for i,d in enumerate(data):
		i = str(i)
		out_str += '<param_'+i+'>'
		out_str += d
		out_str += '</param_'+i+'>'
	out_str += '</resp>'
	return out_str
