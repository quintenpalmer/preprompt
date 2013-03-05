#!/usr/bin/env python
import os
import sys
from pprint import pprint
from pyplib import database

def reload_decks():
	database.delete('game_decks')
	load_decks()
def load_decks():
	for deck in os.listdir(os.path.join('tables','decks')):
		load_deck(deck)
def load_deck(deck_file):
	uid = deck_file.split('.')[0]
	path = os.path.join('tables','decks',deck_file)
	f = open(path,'r')
	for line in f.readlines():
		key,val = line.split(':')
		val = val.rstrip('\n')
	database.insert('game_decks',(int,int,int,str),(None,uid,key,val))

def load_cards():
	path = os.path.join('tables','cards','relation.table')
	f = open(path,'r')
	for line in f.readlines():
		key,val = line.split(':')
		database.insert('game_card_names',(int,str,str),(key,'name',val.strip()))

if len(sys.argv) > 1:
	if sys.argv[1] == 'load':
		if sys.argv[2] == 'all':
			load_cards()
			load_decks()
	elif sys.argv[1] == 'reload':
		if sys.argv[2] == 'all':
			reload_cards()
			reload_decks()
		elif sys.argv[2] == 'cards':
			reload_cards()
		elif sys.argv[2] == 'decks':
			reload_decks()
	elif sys.argv[1] == 'delete':
		sure = raw_input('Are you sure? y/n ')
		if sure == 'y':
			if sys.argv[2] == 'all':
				database.delete('game_decks')
				database.delete('game_card_names')
			elif sys.argv[2] == 'cards':
				database.delete('game_card_names')
			elif sys.argv[2] == 'decks':
				database.delete('game_decks')
			elif sys.argv[2] == 'users':
				database.delete('auth_user')
	elif sys.argv[1] == 'select':
		if len(sys.argv) > 3:
			what = sys.argv[3]
		else:
			what = '*'
		pprint(database.select(sys.argv[2],what))
