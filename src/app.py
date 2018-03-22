from flask import Flask, request
import facebook
import json
from Facebook.FacebookDatabase import FacebookDatabase
from collections import namedtuple

app = Flask(__name__)

# This is a simple user specific token... should be changed to an app or be provided by the API user.
# For simplicity this is a static token 
token = 'EAACEdEose0cBAOaY5zFnqDjXZA6VdvgW1GZCRVvnwBUrwcSRVJ4CVfcp9bvViGqAmPybnRWsTZCYZByxrA8XdP399Ig2v9ARi7ggRWVkjx6j1tXZBnmtrsgo1CZAmTSqJt6j5TnJnFlWp5eXJ5sL4mZBVXnZB5QPkTRYa7rnj3riKLFlFB1PNujh3eZAwf7rVKC8ZD'

# Get User
@app.route('/users/<facebookId>')
def scrapUser(facebookId):
	f = FacebookDatabase()
	if request.args.get("local") != "true":
		try:
			graph = facebook.GraphAPI(access_token=token, version="2.12")
			user = graph.get_object(id = facebookId, fields='id,name,gender')
			userobj = namedtuple("user", user.keys())(*user.values())
			f.insertUser(userobj)
		except facebook.GraphAPIError as e:
			return e.message
	else:
		user = f.getUser(facebookId)
	return json.dumps(user)

# Get User's Posts
@app.route('/users/<facebookId>/posts')
def getLastPosts(facebookId):
	f = FacebookDatabase()
	if request.args.get("local") != "true":
		try:
			graph = facebook.GraphAPI(access_token=token, version="2.12")
			posts = graph.get_object(id = facebookId, fields='posts.limit(25)')
			posts = posts['posts']['data']
			for p in posts:
				post = f.cleanPost(p)
				postobj = namedtuple("post", post.keys())(*post.values())
				f.insertPost(postobj)
		except facebook.GraphAPIError as e:
			return e.message
	else:
		if request.args.get("limit") == None or request.args.get("page") == None:
			return "Error"
		else:
			posts = f.getPosts(facebookId, request.args.get("limit"), request.args.get("page"))
	return json.dumps(posts)

# List saved users
@app.route('/localusers')
def getLocalUsersList():
	f = FacebookDatabase()
	if request.args.get("limit") == None or request.args.get("page") == None:
		return "Error"
	else:
		posts = f.getUsers(request.args.get("limit"), request.args.get("page"))
	return json.dumps(posts)


if __name__ == '__main__':
	app.run()