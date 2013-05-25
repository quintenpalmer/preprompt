#!/usr/bin/env python

import os
import re
import glob

delim = "~"

space_reduce = re.compile(r' +')
base_path = os.path.join(os.environ['postprompt'],'src','postprompt')

pre_glob_path = os.path.join(base_path,'*.go')
gofiles = glob.glob(pre_glob_path)
#gofiles = [os.path.join(base_path,'player.go')]

structs = {}

class Struct:
	def __init__(self,name):
		self.name = name
		self.fields = []
		self.methods = []
	def __repr__(self):
		method_text = '\n\tmethod : '
		field_text = '\n\tfield : '
		return '%s :%s%s'%(self.name,method_text+method_text.join(self.methods) if self.methods != [] else '',field_text+field_text.join(self.fields) if self.fields != [] else '')

def print_type(line):
	if not line[1] in structs:
		structs[line[1]] = Struct(line[1])
	if line[2] not in ('struct','interface'):
		structs[line[1]].fields.append(line[-1].lstrip('*'))

def print_func(line):
	if line[1] == '(':
		structname = line[3].lstrip('*')
		if not structname in structs:
			structs[structname] = Struct(structname)
		structs[structname].methods.append(line[5])
	else:
		#print 'method %s'%line[1]
		pass

def print_field(line,structname):
	if not structname in structs:
		structs[structname] = Struct(structname)
	if line[1] == 'map':
		structs[structname].fields.append(line[5].lstrip('*'))
	elif line[1] == '[':
		if line[2] == ']':
			structs[structname].fields.append(line[3].lstrip('*'))
		else:
			if line[4] == '[':
				structs[structname].fields.append(line[7].lstrip('*'))
			else:
				structs[structname].fields.append(line[4].lstrip('*'))
	elif line[1] == '(':
		structs[structname].fields.append(line[0].lstrip('*'))
	else:
		structs[structname].fields.append(line[1].lstrip('*'))

def format_line(line):
	line = line.strip()
	line = re.sub(space_reduce,' ',line)
	line = re.sub(r"([,{\(\[}\)\]])",delim+r"\1"+delim,line)
	line = re.sub(r" +",delim,line)
	line = re.sub(delim+"+",delim,line)
	line = line.split(delim)
	return line

for gofile in gofiles:
	with open(gofile,'r') as f:
		in_struct = False
		in_interface = False
		for line in f:
			line = format_line(line)
			keyword = line[0]
			if keyword == 'type':
				print_type(line)
				if len(line) > 3 and line[2] == 'struct' and line[-2] != '}':
					in_struct = True
					structname = line[1]
				elif len(line) > 3 and line[2] == 'interface' and line[-2] != '}':
					in_interface = True
					ifacename = line[1]
			elif keyword == 'func':
				print_func(line)
			elif in_struct:
				if line[1] == '}':
					in_struct = False
					continue
				print_field(line,structname)
			elif in_interface:
				if line[1] == '}':
					in_interface = False
					continue
				print_field(line,ifacename)

for key,val in structs.items():
	print val
