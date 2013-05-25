import json

class PPjo:
	def __init__(self,string=None,obj=None,filename=None):
		if string is not None:
			self.obj = json.loads(string)
		elif filename is not None:
			with open(filename) as f:
				self.obj = json.load(f)
		elif obj is not None:
			self.obj = obj

	def get_object(self,tag):
		return PPjo(obj=self.obj.get(tag))

	def get_string(self,tag):
		return str(self.obj.get(tag)).replace("u\'","\'").replace("\'","\\\"")

	def get_strings(self,tag):
		return list([str(i) for i in self.obj.get(tag)])

	def get_int(self,tag):
		return int(self.obj.get(tag))

	def get_ints(self,tag):
		return list([int(i) for i in self.obj.get(tag)])

	def get_bool(self,tag):
		return self.obj.get(tag) == 'true'

	def get_objects(self,tag):
		return list([PPjo(obj=obj) for obj in self.obj.get(tag)])

	def __repr__(self):
		return self.obj
