#!/usr/bin/env python
import os
import sys
from pprint import pprint

from pplib.database import Database
from pplib import json_parser
from pplib.manage_db import register_add_cards

pplib_path = os.path.join(os.environ['postprompt'],'web')
sys.path.insert(0,pplib_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
from django.contrib.auth.models import User

base_path = os.path.join(os.environ['postpromptroot'],'opt','postprompt','tables')

class DatabaseController:
	def __init__(self):
		self.db = Database()
	def reload_cards(self):
		self.delete_cards()
		self.load_cards()
	def delete_cards(self):
		self.db.delete('play_cards')
		self.db.delete('play_starting_cards')
		self.db.delete('play_card_names')
	def load_cards(self):
		path = os.path.join(base_path,'cards','all.json')
		obj = json_parser.create_object(path)
		cards = json_parser.get_array(obj,'cards')
		for key,card in enumerate(cards):
			key += 1
			name = json_parser.get_string(card,"name")
			effect = json_parser.get_string(card,"effect")
			self.db.update('insert into play_card_names values(%s,"%s","%s")'%(key,name,effect))

		path = os.path.join(base_path,'cards','starting.json')
		obj = json_parser.create_object(path)
		card_ids = json_parser.get_array(obj,'card_ids')
		for key,card_id in enumerate(card_ids):
			key += 1
			self.db.update("insert into play_starting_cards values(%s,%s)"%(key,card_id))

	def reload_users(self):
		self.delete_users()
		self.load_users()
	def delete_users(self):
		self.db.delete('auth_user')
	def load_users(self):
		path = os.path.join(base_path,'users','all.json')
		obj = json_parser.create_object(path)
		users = json_parser.get_array(obj,'users')
		for user in users:
			username = json_parser.get_string(user,"username")
			password = json_parser.get_string(user,"password")
			email = json_parser.get_string(user,"email")
			User.objects.create_user(username,email,password)
			register_add_cards(username)

	def delete_games(self):
		self.db.delete('play_games')

	def delete_all(self):
		self.delete_games()
		self.delete_users()
		self.delete_cards()

	def load_all(self):
		self.load_cards()
		self.load_users()

	def reload_all(self):
		self.reload_cards()
		self.reload_users()

dbc = DatabaseController()

commands = {
	'games' : { 'delete' : dbc.delete_games },
	'cards' : { 'delete' : dbc.delete_cards , 'load' : dbc.load_cards, 'reload' : dbc.reload_cards },
	'users' : { 'delete' : dbc.delete_users , 'load' : dbc.load_users, 'reload' : dbc.reload_users },
	'all' : { 'delete' : dbc.delete_all , 'load' : dbc.load_all, 'reload' : dbc.reload_all },
}

def help_text():
	ret = "Database Controlling Tool  - Usage :\n"
	ret += "  ppdbctl.py <table> <command>\n"
	for key,val in commands.items():
		ret += '    %0-8s'%key
		ret += '[ '
		ret += ' | '.join(val.keys())
		ret += ' ]'
		ret += '\n'
	ret = ret[:-1]
	return ret

if __name__ == "__main__":
	if len(sys.argv) > 1:
		if sys.argv[1] in commands.keys():
			table = commands[sys.argv[1]]
			if sys.argv[2] in table.keys():
				table[sys.argv[2]]()
		elif sys.argv[1] == 'select':
			if len(sys.argv) > 3:
				what = sys.argv[3]
			else:
				what = '*'
			for line in dbc.db.select('select %s from %s'%(what,sys.argv[2])):
				for entry in line:
					print '%-15s'%entry,
				print ''
		else:
			print help_text()
	else:
		print help_text()
