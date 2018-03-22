import psycopg2
from psycopg2.extras import RealDictCursor
from .config import config

# Handles the connection with postgres and executions
class PostgresManager(object):
	conn = None
	cur = None

	def __init__(self):
		if self.conn != None:
			return
		try:
			params = config()
			self.conn = psycopg2.connect(**params)
			#self.cur = self.conn.cursor()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
			raise ValueError('DB Connection Error')

	def close(self):
		if self.conn == None:
			return
		try:
			if self.conn == None:
				raise ValueError('DB not Initialized to close')
			self.conn.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
			raise ValueError('DB Connection close Error')
		finally:
			self.conn = None
			self.cur = None

	def commit(self):
		try:
			if self.conn == None:
				raise ValueError('DB not Intialize to commit')
			self.conn.commit()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
			raise ValueError('DB commit Error')
	
	def executeCommand(self, command, param=None):
		try:
			if self.conn == None:
				raise ValueError('DB Not Intialized to Execute')
			if self.cur == None:
				self.cur = self.conn.cursor()
			self.cur.execute(command, param)
			self.cur.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
			raise ValueError('DB execution Error')
		finally:
			self.cur = None
	
	def selectCommand(self, command, param):
		try:
			if self.conn == None:
				raise ValueError('DB Not Intialized to Execute')
			self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
			self.cur.execute(command, param)
			return self.cur.fetchall()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
			raise ValueError('DB execution Error')
		finally:
			self.cur = None