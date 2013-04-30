#!/usr/bin/env python
import os
import sys
from pprint import pprint

from pplib import database
from pplib.manage_db import register_add_cards

pplib_path = os.path.join(os.environ['postprompt'],'web')
sys.path.insert(0,pplib_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
from django.contrib.auth.models import User

base_path = os.path.join(os.environ['postpromptroot'],'opt','postprompt','tables')

def reload_cards():
	delete_cards()
	load_cards()
def delete_cards():
	database.delete('play_cards')
	database.delete('play_starting_cards')
	database.delete('play_card_names')
def load_cards():
	path = os.path.join(base_path,'cards','all.table')
	f = open(path,'r')
	for key,line in enumerate(f.readlines()):
		key = key+1
		val = line.strip()
		database.insert('play_card_names',(int,str,str),(key,'name',val))
	def load_starting_cards():
		path = os.path.join(base_path,'cards','starting.table')
		f = open(path,'r')
		line = f.readlines()[0].strip()
		for val in line.split(','):
			database.insert('play_starting_cards',(int,int),(None,val))
	load_starting_cards()

def reload_users():
	delete_users()
	load_users()
def delete_users():
	database.delete('auth_user')
def load_users():
	path = os.path.join(base_path,'users','all.table')
	f = open(path,'r')
	def add_user(username,password,email):
		User.objects.create_user(username,email,password)
		register_add_cards(username)
	for line in f.readlines():
		upe = line.strip().split(',')
		username = upe[0]
		password = upe[1]
		email = upe[2]
		add_user(username,password,email)

def delete_games():
	database.delete('play_games')

def delete_all():
	delete_games()
	delete_users()
	delete_cards()

def load_all():
	load_cards()
	load_users()

def reload_all():
	reload_cards()
	reload_users()

mapping = {
	'games' : { 'delete' : delete_games },
	'cards' : { 'delete' : delete_cards , 'load' : load_cards, 'reload' : reload_cards },
	'users' : { 'delete' : delete_users , 'load' : load_users, 'reload' : reload_users },
	'all' : { 'delete' : delete_all , 'load' : load_all, 'reload' : reload_all },
}

def help_text():
	ret = "Database Controlling Tool  - Usage :\n"
	for key,val in mapping.items():
		ret += '\t%0-8s'%key
		ret += '[ '
		for subkey in val.keys():
			ret += '%0-7s'%(subkey+',')
		ret = ret[:-1]
		ret += ' ]'
		ret += '\n'
	ret = ret[:-1]
	return ret

if __name__ == "__main__":
	if len(sys.argv) > 1:
		if sys.argv[1] in mapping.keys():
			table = mapping[sys.argv[1]]
			if sys.argv[2] in table.keys():
				table[sys.argv[2]]()
			elif sys.argv[2] == 'select':
				if len(sys.argv) > 3:
					what = sys.argv[3]
				else:
					what = '*'
				pprint(database.select(table,what))
		else:
			print help_text()
