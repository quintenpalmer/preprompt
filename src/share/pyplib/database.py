import sqlite3
import os
from pyplib.errors import PP_Database_Error

def init():
	database_path = os.path.join(os.environ['pyproot'],'opt','postprompt','shared_database')
	con = sqlite3.connect(database_path)
	cur = con.cursor()
	return (con,cur)

def insert_batch(table_name,types,values_list):
	#try:
	if True:
		con,cur = init()
		class Namespace(): pass
		ns = Namespace()
		try:
			ns.key = int(select(table_name,'id')[-1])+1
		except PP_Database_Error and IndexError:
			ns.key = 0
		def get_next_key(ns_sub):
			ret = ns_sub.key
			ns_sub.key += 1
			return ret
		for values in values_list:
			values = tuple([value if value != None else get_next_key(ns) for value in values])
			if True:
				command = "insert into "+table_name+" values("
				for t in types:
					if t == int:
						command+="%s,"
					elif t == str:
						command+= "'%s',"
					else:
						raise Exception ('Unknown data type')
				command = command[:-1]
				command += ")"
				command = command%values
				print command
				cur.execute(command)
				con.commit()
	#except sqlite3.OperationalError:
	#	raise PP_Database_Error("Database Error (database doesn't exist)")

def insert(table_name,types,values):
	con,cur = init()
	def get_next_key():
		try:
			keys = select(table_name,'id')
			return str(int(keys[-1])+1)
		except PP_Database_Error and IndexError:
			return '0'
	values = tuple([value if value != None else get_next_key() for value in values])
	#try:
	if True:
		command = "insert into "+table_name+" values("
		for t in types:
			if t == int:
				command+="%s,"
			elif t == str:
				command+= "'%s',"
			else:
				raise Exception ('Unknown data type')
		command = command[:-1]
		command += ")"
		command = command%values
		print command
		cur.execute(command)
		con.commit()
	#except sqlite3.OperationalError:
	#	raise PP_Database_Error("Database Error (database doesn't exist)")

def update(table_name,set_name,set_value,type,checks):
	con,cur = init()
	#try:
	if True:
		if type == str:
			quote = "'"
		else:
			quote = ''
		command = 'update '+table_name+' set '+set_name+"="+quote+set_value+quote+" where "
		for key,value in checks:
			command += str(key)+"="+str(value)+" and "
		command = command[:-4]
		print command
		cur.execute(command)
		con.commit()
	#except sqlite3.OperationalError:
	#	raise PP_Database_Error("Database Error (database doesn't exist)")

def select(table_name,name,where=None):
	con,cur = init()
	#try:
	if True:
		command = 'select '+name+' from '+table_name
		if where != None:
			command += ' where '
			for w in where:
				command += w+' and '
			command = command[:-4]
		print command
		cur.execute(command)
		ret = cur.fetchall()
		if name != '*' and ',' not in name:
			return [retval[0] for retval in ret]
		else:
			return ret
	#except sqlite3.OperationalError:
	#	raise PP_Database_Error("Database Error (database doesn't exist)")

def delete(table_name,where=None):
	con,cur = init()
	#try:
	if True:
		command = 'delete from '+table_name
		if where != None:
			command += ' where '
			for w in where:
				command += w+' and '
			command = command[:-4]
		cur.execute(command)
		con.commit()
	#except sqlite3.OperationalError:
	#	raise PP_Database_Error("Database Error (database doesn't exist)")

def in_table(table_name,name,value):
	return str(value) in database.select(tabel_name,name)
