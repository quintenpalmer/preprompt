#!/usr/bin/env python
import re

class Diagram:
	def __init__(self):
		self.root = None
		self.dclasses = []
	def add(self,dclass):
		if self.root is None:
			self.root = dclass
		self.dclasses.append(dclass)
	def link(self):
		for dclass in self.dclasses:
			dclass.create_links(self.dclasses)
	def draw(self,module=None,depth=None,methods=True):
		if module is not None:
			module = self.root.find_module(module)
		else:
			module = self.root
		module.draw(depth=depth,methods=methods)
	def __repr__(self):
		ret = ''
		for dclass in self.dclasses:
			ret += dclass.__repr__()+'\n'
		ret.rstrip()
		return ret

class DiagramClass:
	def __init__(self,name,color=True):
		self.name = name
		self.fields = []
		self.methods = []
		self.TODO = None
		self.color = color
	def add_field(self,name,count):
		self.fields.append(DiagramField(name,count))
	def add_method(self,name,*params):
		self.methods.append(DiagramMethod(name,*params))
	def add_TODO(self,name):
		self.TODO = name
	def create_links(self,classes):
		for field in self.fields:
			for dclass in classes:
				if field.name == dclass.name:
					field.add_link(dclass)
					break
		self.num_fields = len([f for f in self.fields if f.has_link])
	def get_box(self,prefix='',extension='',methods=True):
		self.extension = extension
		self.prefix = prefix

		length = max(0,len(self.name),*[len(field.name) for field in self.fields])
		if methods:
			length = max(0,length,*[len(field.name) for field in self.methods])
		self.length = length + 4

		def empty_space():
			return '%s %s %s\n'%(self.prefix,' '*self.length,self.extension)
		def seperator():
			return '%s+%s+%s\n'%(self.prefix,'-'*self.length,self.extension)
		def blank_row():
			return '%s|%s|%s\n'%(self.prefix,' '*self.length,self.extension)
		def create_row(name,color='0',color_start=0,new_extension=''):
			return '%s| %s%s%s%s%s|%s\n'%(
				self.prefix,
				name[0:color_start],
				'\33[%sm'%color if self.color else '',
				name[color_start:None],
				'\33[0m' if self.color else '',
				' '*(self.length-len(name)-1),
				new_extension if new_extension != '' else self.extension,
			)
		def add_name(name):
			return create_row(name,color='34')
		def add_members(name,members):
			ret = create_row(name,color='32')
			for member in members:
				name = member.name
				if hasattr(member,'has_link') and member.has_link:
					ret += create_row('- '+name,color='31',color_start=2,new_extension='-'*len(self.extension)+'--+')
					self.extension+='  |'
				else:
					ret += create_row('- '+name,color='31',color_start=2)
			return ret

		return '%s'*8%(
			seperator(),
			add_name(self.name),
			seperator(),
			add_members('Fields',[field for field in self.fields]),
			seperator(),
			add_members('Methods',[method for method in self.methods]) if methods else '',
			seperator() if methods else '',
			empty_space(),
		)

	def draw(self,prefix='',extension='',depth=None,methods=True):
		subclasses = []
		for field in self.fields:
			if field.has_link:
				subclasses.append(field.link)
		print self.get_box(prefix,extension,methods=methods).rstrip()+'\n',
		indent = prefix + ' '*(self.length+4) + '|  '*(self.num_fields-1)
		prev_length = 0
		for s in reversed(subclasses):
			if depth is None or depth > 0:
				s.draw(prefix=indent,extension=' '*prev_length,depth=depth-1 if depth is not None else None,methods=methods)
				prev_legnth = s.length
				indent = indent[:-3]

	def find_module(self,name):
		if self.name == name:
			return self
		else:
			for child in self.fields:
				if child.has_link:
					module = child.link.find_module(name)
					if module != None:
						return module

	def __repr__(self):
		return "%s %s %s %s"%(
			self.name,
			self.fields,
			self.methods,
			'TODO : %s'%self.TODO if self.TODO else ''
		)

class DiagramField:
	def __init__(self,name,count):
		self.name = name
		self.count = count
		self.has_link = False
	def add_link(self,dclass):
		self.has_link = True
		self.link = dclass
	def __repr__(self):
		return "%s (%s) [%s]"%(self.name,self.count,'type' if self.has_link else 'prim')

class DiagramMethod:
	def __init__(self,name,*params):
		self.name = name
		self.params = params
	def __repr__(self):
		return "%s%s"%(self.name,self.params)

def read_diagram(filename='DIAGRAM',color=True):
	diagram = Diagram()
	current_class = None

	diagram_file = open(filename,'r')
	for line in diagram_file:
		line = line.rstrip()
		if re.search('^\w',line):
			if current_class != None:
				diagram.add(current_class)
			current_class = DiagramClass(line.split(':')[0].rstrip(),color=color)
		if re.search('^\t\w',line):
			fmtype, name = [l.strip() for l in line.lstrip('\t').split(':')]
			if fmtype == 'field':
				tmp = name.split(' ')
				name = tmp[0]
				if len(tmp) == 2:
					count = tmp[1].rstrip(')').lstrip('(')
				else:
					count = 1
				current_class.add_field(name,count)
			elif fmtype == 'method':
				tmp = name.split(' ')
				name = tmp[0]
				params = tmp[1:]
				current_class.add_method(name,*params)
			elif fmtype == 'TODO':
				current_class.add_TODO(name)
	diagram.add(current_class)

	diagram.link()
	return diagram

if __name__ == "__main__":
	import sys
	import os
	color = 'color' in os.environ['TERM']

	filename = 'DIAGRAM'
	module = None
	methods = True
	depth = None
	param_depth = None
	for arg in sys.argv[1:]:
		if arg[:3] == '-f=':
			filename = arg[3:]
		elif arg[:3] == '-c=':
			module = arg[3:]
		elif arg[:2] == '-a':
			param_depth = None
		elif arg[:2] == '-o':
			param_depth = 0
		elif arg[:2] == '-p':
			color = True
		elif arg[:2] == '-u':
			color = False
		elif arg[:2] == '-m':
			methods = True
		elif arg[:2] == '-n':
			methods = False
		elif re.search('-\d',arg[:2]):
			param_depth = arg[1:]
	if param_depth != None:
		depth = int(param_depth)
	diagram = read_diagram(filename,color)

	diagram.draw(module=module,depth=depth,methods=methods)
