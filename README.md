# Ofaly Task Facebook API using Flask and Python

### Endpoints
(All Endpoints have optional ?local parameter)

#### GET /users/<facebookId>
This gets the user data (id, name, gender) & saves on DB with optional 

#### GET /users/<facebookId>/posts
Gets last 25 posts with pagination.
You must provide both limit and page parameter

#### GET /users/
Gets list of saved users on DB

## How to run
1. pip install -r requirements.txt (or use setup.py)
2. python app.py from src directory

# Note change the token in app.py for your own app or user token
# I reccommend using the auth_url to generate a FB login page to get token
