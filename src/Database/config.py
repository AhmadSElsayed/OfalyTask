from configparser import ConfigParser
import os

# Reads database configuration from "database.ini with section [postgresql]" 
def config(filename='database.ini', section='postgresql'):
	script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
	filename = os.path.join(script_dir, filename)
	
	parser = ConfigParser()
	parser.read(filename)
	db = {}
	if parser.has_section(section):
		params = parser.items(section)
		for param in params:
			db[param[0]] = param[1]
	else:
		raise Exception('Section {0} not found in the {1} file'.format(section, filename))
	return db

