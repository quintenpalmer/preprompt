#!/usr/bin/env python
import subprocess as sub
import sys

if len(sys.argv)==2:
	start = int(sys.argv[1])
else:
	start = 0

out = sub.check_output(['ls','-pR'])
full = []
excludes = ['crx','deb','zip','class','pyc','jar','dylib','jnilib','so','dll']
concat = ''
for line in out.split('\n'):
	if line[-1:]==':':
		if line=='.:':
			concat = ''
		else:
			concat = line[:-1].lstrip('.').lstrip('/')+'/'
	else:
		if line.strip()!='' and not '/' in line and line.strip()!='alldata.txt' and line.split('.')[-1] not in excludes:
			full.append(concat+line)
f = open('alldata.txt','w')
for line in full[start:]:
	print line
	sub.call(['vi',line])
	q = raw_input("hit q to quit")
	if q == 'q':
		break
	'''
	f.write('-'*30+'\n')
	f.write(line+'\n')
	f.write('-'*10+'\n')
	f.write(sub.check_output(['cat',line])+'\n')
	'''
f.close()
