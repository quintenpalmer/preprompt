#!/usr/bin/env python
import os
import sys
from pyplib import database

def load_cards():
	path = os.path.join('tables','cards','relation.table')
	f = open(path,'r')
	for line in f.readlines():
		key,val = line.split(':')
		database.insert('game_cards',(int,str,str),(key,'name',val.strip()))

if len(sys.argv) > 1:
	if sys.argv[1] == 'reload':
		database.drop('game_cards')
		load_cards()
	elif sys.argv[1] == 'load':
		load_cards()
	elif sys.argv[1] == 'select':
		if len(sys.argv) > 2:
			what = sys.argv[2]
		else:
			what = '*'
		print database.select('game_cards',what)
	elif sys.argv[1] == 'drop':
		sure = raw_input('Are you sure? y/n ')
		if sure == 'y':
			database.drop('game_cards')
