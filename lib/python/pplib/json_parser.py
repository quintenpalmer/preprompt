import json

from pplib.errors import JsonParserError

class PPjo:
	def __init__(self,obj):
		self.obj = json.loads(obj)

	def get_object(self,tag):
		return PPjo(self.obj.get(tag))

	def get_string(self,tag):
		return str(self.obj.get(tag))

	def get_int(self,tag):
		return int(self.obj.get(tag))

	def get_ints(self,tag):
		return list([int(i) for i in self.obj.get(tag)])

	def get_bool(self,tag):
		return self.obj.get(tag) == 'true'

	def get_objects(self,tag):
		return list([PPjo(obj) for obj in self.obj.get(tag)])

	def __repr__(self):
		return self.obj

def create_object(jstring):
	return json.loads(jstring)

def create_object_from_file(file_name):
	with open(file_name) as f:
		return json.load(f)

def get_object(obj,tag):
	#return create_object(obj.get(tag))
	return obj.get(tag)

def get_string(obj,tag):
	return str(obj.get(tag)).replace("u\'","\'").replace("\'","\\\"")

def get_int(obj,tag):
	return int(obj.get(tag))

def get_bool(obj,tag):
	return obj.get(tag) == 'true'

def get_objects(obj,tag):
	#return [create_object(o) for o in obj.get(tag)]
	return list(obj.get(tag))

def get_ints(obj,tag):
	return [int(i) for i in obj.get(tag)]


