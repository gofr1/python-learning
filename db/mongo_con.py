# pip install pymongo
import configparser
from pymongo import MongoClient
from random import randint


section_name = 'mongo_local'
config = configparser.ConfigParser()
c = config.read("./.env/db.conf")
db_opts = config.options(section_name)
details = dict()

for db_opt in db_opts:
    details[db_opt] = config.get(section_name, db_opt)

# Open connectiob
uri = 'mongodb://{user}:{password}@{host}:{port}/?authSource={authsource}'.format(**details)
client = MongoClient(uri)

# Connect to DB
db=client.test

# Search some document
fivestar = db.zips.find_one({'_id': '01001'})
print(fivestar)

# Close connection
client.close()