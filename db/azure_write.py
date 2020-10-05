from sqlalchemy import create_engine
import urllib, configparser
import pandas as pd

section_name = 'azure_main'
config = configparser.ConfigParser()
c = config.read("./.env/db.conf")
db_opts = config.options(section_name)
details = dict()

for db_opt in db_opts:
    details[db_opt] = config.get(section_name, db_opt)

connect_string = 'DRIVER={driver};SERVER={server};PORT={port};DATABASE={database};UID={uid};PWD={pwd}'.format(**details)

params = urllib.parse.quote_plus(connect_string)

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

df = pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3']})

df.to_sql('users', con=engine, if_exists='replace', index=False)

engine.execute("SELECT * FROM users").fetchall()