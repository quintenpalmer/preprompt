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
	def draw(self):
		self.root.draw()
		#for dclass in self.dclasses:
		#	print dclass.draw()
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
	def get_box(self,prefix='',extension=''):
		self.extension = extension
		self.prefix = prefix

		length = max(0,len(self.name),*[len(field.name) for field in self.fields])
		length = max(0,length,*[len(method.name) for method in self.methods])
		self.length = length + 4

		def empty_space():
			return '%s %s %s\n'%(self.prefix,' '*self.length,self.extension)
		def seperator():
			return '%s+%s+%s\n'%(self.prefix,'-'*self.length,self.extension)
		def blank_row():
			return '%s|%s|%s\n'%(self.prefix,' '*self.length,self.extension)
		def create_row(name,color='0',color_start=0,extension=''):
			return '%s| %s%s%s%s%s|%s\n'%(
				self.prefix,
				name[0:color_start],
				'\33[%sm'%color if self.color else '',
				name[color_start:None],
				'\33[0m' if self.color else '',
				' '*(self.length-len(name)-1),
				extension if extension != '' else self.extension,
			)
		def add_name(name):
			return seperator() + create_row(name,color='34')
		def add_members(name,members):
			ret = seperator()
			ret += create_row(name,color='32')
			for member in members:
				name = member.name
				if hasattr(member,'has_link') and member.has_link:
					ret += create_row('- '+name,color='31',color_start=2,extension='-'*len(self.extension)+'--+')
					self.extension+='  |'
				else:
					ret += create_row('- '+name,color='31',color_start=2)
			return ret

		box = '%s%s%s%s%s'%(
			add_name(self.name),
			add_members('Fields',[field for field in self.fields]),
			add_members('Methods',[method for method in self.methods]),
			seperator(),
			empty_space(),
		)
		return box
	def draw(self,prefix='',extension=''):
		box = self.get_box(prefix,extension)
		subclasses = []
		for field in self.fields:
			if field.has_link:
				subclasses.append(field.link)
		print box,
		num_fields = len([f for f in self.fields if f.has_link])
		indent = prefix + ' '*num_fields+' '*(self.length-(num_fields-4)) + '|  '*(num_fields-1)
		old = self
		for s in reversed(subclasses):
			s.draw(prefix=indent,extension=' '*old.length if hasattr(self,'old') else ''),
			old = s
			indent = indent[:-3]
	def __repr__(self):
		return "%s %s %s %s"%('\33[31m%s\33[0m'%self.name if self.color else self.name,self.fields,self.methods,'TODO : %s'%self.TODO if self.TODO else '')

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
				current_class.add_method(name)
			elif fmtype == 'TODO':
				current_class.add_TODO(name)
	diagram.add(current_class)

	diagram.link()
	#print diagram
	diagram.draw()

if __name__ == "__main__":
	import sys
	import os
	filename = sys.argv[1] if len(sys.argv) > 1 else 'DIAGRAM'
	color = 'color' in os.environ['TERM']
	read_diagram(filename,color)
