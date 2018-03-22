from .PostgresManager import PostgresManager

# Intializes the schema dynamicaly to fit the API needs
class DatabaseInitializer(object):
	def initializeDB(self):
		""" create tables in the PostgreSQL database"""
		commands = (
			"drop table post;", "drop table facebookuser;"
			"""
			CREATE TABLE FacebookUser (
				id varchar(1000) PRIMARY KEY,
				name varchar(1000) NOT NULL,
				gender varchar(10) not null
			);
			""",
			""" CREATE TABLE Post (
					userId varchar(1000) references FacebookUser(id) not null,
					postId varchar(1000) unique not null,
					story varchar(1000) NOT NULL,
					message varchar(1000) NULL,
					created_time varchar(1000) not null
					);
			""")
		try:
			ps = PostgresManager()
			for command in commands:
				ps.executeCommand(command, None)
			ps.commit()
			ps.close()
		except ValueError as e:
			print(e.args)