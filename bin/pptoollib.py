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
	def __init__(self,name,help_text,func,*args):
		self.name = name
		self.help_text = help_text
		self.func = func
		self.args = args

class PPParse:
	def __init__(self):
		self.flags = []
		self.commands = []
	def add_flag(self,flag,help_text,field,value,default=NoDefault()):
		flag = Flag(flag,help_text,field,value,default)
		self.flags.append(flag)
		if type(flag.default) != type(NoDefault()):
			setattr(self,flag.field,flag.default)
	def add_command(self,name,help_text,*args):
		self.commands.append(Command(name,help_text,*args))
	def help_text(self,invalid = None):
		if invalid != None:
			sys.stdout.write('Invalid flag %s\n'%invalid)
		sys.stdout.write('Usage :\n')
		sys.stdout.write('%s %s<option>\n'%(sys.argv[0].split('/')[-1],'<command> ' if len(self.commands) != 0 else ''))
		for command in self.commands:
			sys.stdout.write('    %s - %s\n'%(command.name,command.help_text))
		for flag in self.flags:
			sys.stdout.write('    %0-4s - %s\n'%(flag.flag,flag.help_text))
	def parse(self):
		for arg in sys.argv[1:]:
			found = False
			for flag in self.flags:
				if arg.startswith(flag.flag):
					found = True
					setattr(self,flag.field,flag.value(arg))
			for command in self.commands:
				if arg == command.name:
					found = True
					command.func(*command.args)
			if not found:
				self.help_text(invalid=arg)
				sys.exit(1)
