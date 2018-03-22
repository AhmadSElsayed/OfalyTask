import unittest
from src.Facebook.FacebookDatabase import FacebookDatabase
from collections import namedtuple
import json

class FacebookTest(unittest.TestCase):
	def setUp(self):
		pass
	
	def Test_InsertUser(self):
		f = FacebookDatabase()
		user = {'id': "0", 'name' : "Test", 'gender' : "T"}
		user_named = namedtuple("user", user.keys())(*user.values())
		self.assertIsNotNone(f.insertUser(user_named))
		dbUser = f.getUser(user_named.id)
		self.assertEqual(json.dumps(dbUser), json.dumps(user_named))

	def Test_InsertPost(self):
		f = FacebookDatabase()
		post = {'userId': "0", 'postId': "0", 'story': "Test", 'message': "Test", "created_time": "Test"}
		post_named = namedtuple("post", post.keys())(*post.values())
		self.assertIsNone(f.insertPost(post_named))

if __name__ == '__main__':
	unittest.main()