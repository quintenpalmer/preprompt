import sys

class NoDefault:
	pass

class Arg:
	def __init__(self,flag,help_text,field,value,default):
		self.flag = flag
		self.help_text = help_text
		self.field = field
		self.value = value
		self.default = default

class PPParse:
	def __init__(self):
		self.args = []
	def add_arg(self,flag,help_text,field,value,default=NoDefault()):
		arg = Arg(flag,help_text,field,value,default)
		self.args.append(arg)
		if type(arg.default) != type(NoDefault()):
			setattr(self,arg.field,arg.default)
	def help_text(self,invalid = None):
		if invalid != None:
			sys.stdout.write('Invalid flag %s\n'%invalid)
		sys.stdout.write('Help text :\n')
		for arg in self.args:
			sys.stdout.write('    %0-4s %s\n'%(arg.flag,arg.help_text))
	def parse(self):
		for sarg in sys.argv[1:]:
			found = False
			for arg in self.args:
				if sarg.startswith(arg.flag):
					found = True
					setattr(self,arg.field,arg.value(sarg))
			if not found:
				self.help_text(invalid=sarg)
				sys.exit(1)
