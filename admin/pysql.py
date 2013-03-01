#!/usr/bin/env python
import sqlite3
import sys
from pprint import pprint

if len(sys.argv) > 1:
	if sys.argv[1] == 'all':
		command = "select name from sqlite_master WHERE type='table'"
	elif sys.argv[1] == 'select':
		if len(sys.argv) > 3:
			what = sys.argv[3]
		else:
			what = '*'
		command = 'select '+what+' from '+sys.argv[2]
	else:
		command = 'select username from auth_user'
else:
	command = 'select username from auth_user'

con = sqlite3.connect('/home/quinten/fun/games/postprompt/root/opt/postprompt/database')
cur = con.cursor()
cur.execute(command)
pprint(cur.fetchall())
