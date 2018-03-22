from Database.PostgresManager import PostgresManager

# This is the class the handles facebook databse transactions
class FacebookDatabase(object):

	# Insert a User into the database
	def insertUser(self, user):
		sql = """INSERT INTO FacebookUser (id, name, gender) VALUES (%s, %s, %s)
		On conflict(id) do update set name = excluded.name, gender = excluded.gender;
		"""
		param = (user.id, user.name, user.gender)
		ps = PostgresManager()
		ps.executeCommand(sql, param)
		ps.commit()
		ps.close()

	# Insert A post into the database
	def insertPost(self, post):
		sql = """INSERT INTO Post(userId, postId, story, message, created_time) VALUES(%s, %s, %s, %s, %s)
		on conflict(postId) do update set story = excluded.story,  message = excluded.message, created_time = excluded.created_time;
		"""
		param = (post.userId, post.postId, post.story, post.message, post.created_time)
		ps = PostgresManager()
		ps.executeCommand(sql, param)
		ps.commit()
		ps.close()

	# gets the facebook post structure and changes it into 
	# a more appropriate form for searching and indexing
	def cleanPost(self, post):
		s = post['id']
		s = s.split("_")
		if "message" in post:
			m = post['message']
		else:
			m = ""
		if "story" in post:
			st = post['story']
		else:
			st = ""
		return {'userId': s[0], 'postId':s[1], 'story':st , 'message':m, 'created_time': post['created_time']}

	# Get List of user from database (paginated)
	# limit -> size of users per page
	# page -> page number (starts from one)
	def getUsers(self, limit, page):
		ps = PostgresManager()
		data = ps.selectCommand("Select * from facebookuser LIMIT %s OFFSET %s", (limit, str((int(limit) * (int(page) - 1)))))
		ps.close()
		return data

	# Get List of posts of a specific user from database (paginated)
	# limit -> size of posts per page
	# page -> page number (starts from one)
	def getPosts(self, userId, limit, page):
		ps = PostgresManager()
		data = ps.selectCommand("Select * from post where userId = %s LIMIT %s OFFSET %s", (userId, int(limit), (int(limit) * (int(page) - 1))))
		ps.close()
		return data

	# Get a specific user data from its ID
	def getUser(self, id):
		ps = PostgresManager()
		return ps.selectCommand("Select * from facebookuser where id = %s", (id,))