#!/usr/bin/env python
import os
import sys
from pprint import pprint
from pyplib import database

def reload_decks():
	pass
	"""
	database.delete('play_decks')
	load_decks()
	"""
def load_decks():
	pass
	"""
	for deck in os.listdir(os.path.join(os.environ['pyproot'],'opt','postprompt','tables','decks')):
		load_deck(deck)
	"""
def load_deck(deck_file):
	uid = deck_file.split('.')[0]
	path = os.path.join(os.environ['pyproot'],'opt','postprompt','tables','decks',deck_file)
	f = open(path,'r')
	for line in f.readlines():
		key,val = line.split(':')
		val = val.rstrip('\n')
	database.insert('play_decks',(int,int,int,str),(None,uid,key,val))

def reload_cards():
	database.delete('play_card_names')
	database.delete('play_cards')
	database.delete('play_starting_cards')
	load_cards()
	load_starting_cards()
def load_cards():
	path = os.path.join(os.environ['pyproot'],'opt','postprompt','tables','cards','all.table')
	f = open(path,'r')
	for key,line in enumerate(f.readlines()):
		val = line.strip()
		database.insert('play_card_names',(int,str,str),(key,'name',val))
	load_starting_cards()

def load_starting_cards():
	path = os.path.join(os.environ['pyproot'],'opt','postprompt','tables','cards','starting.table')
	f = open(path,'r')
	line = f.readlines()[0].strip()
	for val in line.split(','):
		database.insert('play_starting_cards',(int,int),(None,val))

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
				database.delete('play_decks')
				database.delete('play_card_names')
			elif sys.argv[2] == 'cards':
				database.delete('play_card_names')
				database.delete('play_card_names')
			elif sys.argv[2] == 'decks':
				database.delete('play_decks')
			elif sys.argv[2] == 'users':
				database.delete('auth_user')
			elif sys.argv[2] == 'games':
				database.delete('play_games')
	elif sys.argv[1] == 'select':
		if len(sys.argv) > 3:
			what = sys.argv[3]
		else:
			what = '*'
		pprint(database.select(sys.argv[2],what))
