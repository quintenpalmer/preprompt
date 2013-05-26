#!/usr/bin/env python
import os
import sys
import glob
from pprint import pprint

from pplib.json_parser import PPjo
from pplib.database import Database
from pplib.manage_db import register_add_cards

pplib_path = os.path.join(os.environ['postprompt'],'web')
sys.path.insert(0,pplib_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
from django.contrib.auth.models import User


class DatabaseController:
	def __init__(self):
		self.base_path = os.path.join(os.environ['postprompt'],'tables')
		self.db = Database()
	def reload_cards(self):
		self.delete_cards()
		self.load_cards()
	def delete_cards(self):
		self.db.delete('play_cards')
		self.db.delete('play_starting_cards')
		self.db.delete('play_card_names')
	def load_cards(self):
		self.load_card_info()
		path = os.path.join(self.base_path,'starting_cards.json')
		obj = PPjo(filename=path)
		card_ids = obj.get_strings('card_ids')
		for key,card_id in enumerate(card_ids):
			key += 1
			self.db.update("insert into play_starting_cards values(%s,%s)"%(key,card_id))

	def reload_card_info(self):
		self.delete_card_info()
		self.load_card_info()
	def delete_card_info(self):
		self.db.delete('play_card_names')
	def load_card_info(self):
		pre_glob_path = os.path.join(self.base_path,'cards','*.json')
		card_files = glob.glob(pre_glob_path)
		for card_file in card_files:
			obj = PPjo(filename=card_file)
			card = obj.get_object('card')
			key = obj.get_string('index')
			name = card.get_string('name')
			effect = card.get_string('effect')
			self.db.update('insert into play_card_names values(%s,"%s","%s")'%
				(key,name,effect))

	def reload_users(self):
		self.delete_users()
		self.load_users()
	def delete_users(self):
		self.db.delete('auth_user')
	def load_users(self):
		path = os.path.join(self.base_path,'users.json')
		obj = PPjo(filename=path)
		users = obj.get_objects('users')
		for user in users:
			username = user.get_string("username")
			password = user.get_string("password")
			email = user.get_string("email")
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
	'starting' : { 'delete' : dbc.delete_card_info, 'load' : dbc.load_card_info, 'reload' : dbc.reload_card_info},
	'users' : { 'delete' : dbc.delete_users , 'load' : dbc.load_users, 'reload' : dbc.reload_users },
	'all' : { 'delete' : dbc.delete_all , 'load' : dbc.load_all, 'reload' : dbc.reload_all },
}

def help_text():
	ret = "Database Controlling Tool  - Usage :\n"
	ret += "  ppdbctl.py <table> <command>\n"
	for key,val in commands.items():
		ret += '    %0-10s[ %s ]\n'%(key,' | '.join(val.keys()))
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
