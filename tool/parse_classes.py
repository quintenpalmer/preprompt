#!/usr/bin/env python

import sys
import os
import re

main_model = os.path.join(os.environ['postprompt'],'src','ppbackend','model','mainStruct')
effect_model = os.path.join(os.environ['postprompt'],'src','ppbackend','model','effect')
action_model = os.path.join(os.environ['postprompt'],'src','ppbackend','model','action')

prefixes = (main_model,effect_model,action_model)

in_class = False
for prefix in prefixes:
	group = os.listdir(prefix)
	for class_file in group:
		with open(os.path.join(prefix,class_file)) as class_file:
			for line in class_file:
				if re.search('^public class',line):
					in_class = True
					name = re.search('\w+{',line).group(0).rstrip('{')
					sys.stdout.write('%s :\n'%name)
				if in_class:
					if re.search('^\t[^\t].*[^\(].*;',line):
						name = re.search('^\t\w*',line).group(0)[1:]
						if name in ('LinkedList','ArrayList'):
							name = re.search('<\w*',line).group(0)[1:]+' (N)'
						elif name in ('HashMap',):
							name = re.search('\w*>',line).group(0)[:-1]+' (N)'
						if name == 'public':
							split = line.split(' ')
							name = split[1]
							if name == 'static':
								name = split[2]
						sys.stdout.write('\tfield : %s\n'%name)
					elif re.search('^\tpublic \w+ \w+\(',line):
						funcname = re.search('\w+\(',line).group(0).rstrip('(')
						params = re.search('\(.*\)',line).group(0).lstrip('(').rstrip(')')
						params = params.split(' ')
						params = params[::2]
						sys.stdout.write('\tmethod : %s (%s)\n'%(funcname,','.join(params)))
					elif re.search('^}',line):
						in_class = False
				#sys.stdout.write(line)
