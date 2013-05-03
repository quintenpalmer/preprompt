import sys

class NoDefault:
	pass

class Flag:
	def __init__(self,flag,help_text,field,value,default):
		self.flag = flag
		self.help_text = help_text
		self.field = field
		self.value = value
		self.default = default

class SubCommand:
	def __init__(self,name,help_text):
		self.name = name
		self.help_text = help_text

class Command:
	def __init__(self,name,help_text,*sub_commands):
		self.name = name
		self.help_text = help_text
		self.sub_commands = sub_commands

class PPParse:
	def __init__(self):
		self.flags = []
		self.command = None
	def add_flag(self,flag,help_text,field,value,default=NoDefault()):
		flag = Flag(flag,help_text,field,value,default)
		self.flags.append(flag)
		if type(flag.default) != type(NoDefault()):
			setattr(self,flag.field,flag.default)
	def add_command(self,name,help_text,*sub_commands):
		self.command = Command(name,help_text,*sub_commands)
	def help_text(self,invalid = None):
		if invalid != None:
			sys.stdout.write('Invalid flag %s\n'%invalid)
		sys.stdout.write('Help text :\n')
		sys.stdout.write('%s %s<option>\n'%(sys.argv[0].split('/')[-1],'%s '%self.command if self.command is not None else ''))
		for flag in self.flags:
			sys.stdout.write('    %0-4s %s\n'%(flag.flag,flag.help_text))
	def parse(self):
		for arg in sys.argv[1:]:
			found = False
			for flag in self.flags:
				if arg.startswith(flag.flag):
					found = True
					setattr(self,flag.field,flag.value(arg))
			if not found:
				self.help_text(invalid=arg)
				sys.exit(1)
