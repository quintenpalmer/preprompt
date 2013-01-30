
def serialize(data):
	out_str = '<resp>'
	out_str += '<status_type>'
	out_str += data.pop(0)
	out_str += '</status_type>'
	for i,d in enumerate(data):
		i = str(i)
		out_str += '<param'+i+'>'
		out_str += d
		out_str += '</param'+i+'>'
	out_str += '</resp>'
	return out_str
