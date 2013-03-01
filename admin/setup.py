#!/usr/bin/env python
import os
import sys
from pyplib import database

def load_deck(uid):
	path = os.path.join('tables','decks',str(uid)+'.table')
	f = open(path,'r')
	decks = {}
	for line in f.readlines():
		key,val = line.split(':')
	database.insert('game_decks',(int,int,str),(uid,key,val))

if len(sys.argv) > 2:
	if sys.argv[1] == 'load':
		load_deck(sys.argv[2])
