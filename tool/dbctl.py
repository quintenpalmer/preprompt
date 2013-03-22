#!/usr/bin/env python
import os
import sys
from pprint import pprint

from pyplib import database
from pyplib.manage_db import register_add_cards

pyplib_path = os.path.join(os.environ['pyp'],'web')
sys.path.insert(0,pyplib_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
from django.contrib.auth.models import User

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

def reload_users():
	database.delete('auth_user')
	load_users()
def load_users():
	path = os.path.join(os.environ['pyproot'],'opt','postprompt','tables','users','all.table')
	f = open(path,'r')
	for line in f.readlines():
		upe = line.strip().split(',')
		username = upe[0]
		password = upe[1]
		email = upe[2]
		add_user(username,password,email)

def add_user(username,password,email):
	User.objects.create_user(username,email,password)
	"""
	database.insert('auth_user',(int,str,str,int,str,str,str,str,int,int,str),'1','qwer','2013-03-08 03:57:13.167947','0','qwer','','','quintenpalmer@gmail.com','0','1','2013-03-08 03:57:13.167947')
	"""
	register_add_cards(username)

def reload_games():
	database.delete('play_games')


if len(sys.argv) > 1:
	if sys.argv[1] == 'load':
		if sys.argv[2] == 'all':
			load_cards()
			load_users()
	elif sys.argv[1] == 'reload':
		if sys.argv[2] == 'all':
			reload_games()
			reload_cards()
			reload_users()
		elif sys.argv[2] == 'cards':
			reload_cards()
		elif sys.argv[2] == 'games':
			reload_games()
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
