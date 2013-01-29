
def serialize(data):
	out_str = '<resp>'
	out_str += '<status_type>'
	out_str += data.pop(0)
	out_str += '</status_type>'
	if len(data)==1:
		out_str += '<params>'
		out_str += data.pop(0)
		out_str += '</params>'
	out_str += '</resp>'
	return out_str
