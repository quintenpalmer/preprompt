import json

from pplib.errors import JsonParserError

def create_object(filename):
	with open(filename) as f:
		return json.load(f)

def get_object(obj,tag):
	return obj.get(tag)

def get_string(obj,tag):
	return str(get_object(obj,tag))

def get_int(obj,tag):
	return int(get_object(obj,tag))

def get_array(obj,tag):
	return list(obj.get(tag))
