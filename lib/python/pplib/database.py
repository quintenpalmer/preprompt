import sqlite3
import MySQLdb as mdb
import os

class Database:
	def __init__(self,database_name='pp_shared'):
		self.con = mdb.connect('localhost','developer','jfjfkdkdlslskdkdjfjf',database_name)
		self.cur = self.con.cursor()

	def update(self,command):
		self.cur.execute(command)
		self.con.commit()

	def delete(self,table_name):
		command = 'delete from %s'%(table_name,)
		self.cur.execute(command)
		self.con.commit()

	def select(self,command):
		self.cur.execute(command)
		ret = self.cur.fetchall()
		return ret
